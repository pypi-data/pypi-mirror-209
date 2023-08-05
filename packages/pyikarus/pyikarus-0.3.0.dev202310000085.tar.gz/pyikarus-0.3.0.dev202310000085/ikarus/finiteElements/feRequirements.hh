// SPDX-FileCopyrightText: 2022 The Ikarus Developers mueller@ibb.uni-stuttgart.de
// SPDX-License-Identifier: LGPL-3.0-or-later

#pragma once

#include <iosfwd>
#include <map>
#include <set>
#include <vector>

#include <dune/common/exceptions.hh>

#include <Eigen/Core>

namespace Ikarus {

  // clang-format off
  enum class ScalarAffordances {
    noAffordance,
    mechanicalPotentialEnergy,
    microMagneticPotentialEnergy
  };

  enum class VectorAffordances {
    noAffordance,
    forces,
    microMagneticForces
  };

  enum class MatrixAffordances {
    noAffordance,
    stiffness,
    materialstiffness,
    geometricstiffness,
    stiffnessdiffBucklingVector,
    microMagneticHessian,
    mass
  };

  enum class FEParameter {
    noParameter,
    loadfactor,
    time
  };

  enum class FESolutions {
    noSolution,
    displacement,
    velocity,
    director,
    magnetizationAndVectorPotential
  };

  enum class ResultType {
    noType,
    magnetization,
    gradientNormOfMagnetization,
    vectorPotential,
    divergenceOfVectorPotential,
    BField,
    HField,
    cauchyStress,
    director
  };
  // clang-format on
  std::string getResultType(const ResultType &res);

  struct AffordanceCollectionImpl {
    ScalarAffordances scalarAffordances{ScalarAffordances::noAffordance};
    VectorAffordances vectorAffordances{VectorAffordances::noAffordance};
    MatrixAffordances matrixAffordances{MatrixAffordances::noAffordance};
  };

  template <typename Type>
  concept FEAffordance
      = std::is_same_v<std::remove_cvref_t<Type>, ScalarAffordances> or std::is_same_v<std::remove_cvref_t<Type>,
                                                                                       VectorAffordances> or std::
          is_same_v<std::remove_cvref_t<Type>, MatrixAffordances> or std::is_same_v<std::remove_cvref_t<Type>,
                                                                                    AffordanceCollectionImpl>;

  inline constexpr VectorAffordances forces = VectorAffordances::forces;

  inline constexpr MatrixAffordances stiffness                   = MatrixAffordances::stiffness;
  inline constexpr MatrixAffordances stiffnessdiffBucklingVector = MatrixAffordances::stiffnessdiffBucklingVector;
  inline constexpr MatrixAffordances mass                        = MatrixAffordances::mass;

  inline constexpr ScalarAffordances potentialEnergy = ScalarAffordances::mechanicalPotentialEnergy;

  namespace AffordanceCollections {
    inline constexpr AffordanceCollectionImpl elastoStatics
        = {ScalarAffordances::mechanicalPotentialEnergy, VectorAffordances::forces, MatrixAffordances::stiffness};
  }

  namespace Impl {
    template <typename T>
    struct DeduceRawVectorType {
      static_assert(!std::is_same<T, T>::value, "You should end up in the provided specializations");
    };

    template <typename T>
    struct DeduceRawVectorType<std::reference_wrapper<T>> {
      using Type = T;
    };

    template <typename T>
    struct DeduceRawVectorType<Eigen::Ref<T>> {
      using Type = Eigen::Ref<T>;
    };
  }  // namespace Impl

  template <typename SolutionVectorType_ = std::reference_wrapper<Eigen::VectorXd>,
            typename ParameterType_      = std::reference_wrapper<double>>
  class FErequirements {
  public:
    using SolutionVectorType    = SolutionVectorType_;
    using SolutionVectorTypeRaw = Impl::DeduceRawVectorType<std::remove_cvref_t<SolutionVectorType_>>::Type;
    using ParameterType         = ParameterType_;
    using ParameterTypeRaw      = ParameterType_::type;
    template <FEAffordance Affordance>
    FErequirements &addAffordance(Affordance &&affordance) {
      if constexpr (std::is_same_v<Affordance, ScalarAffordances>)
        affordances.scalarAffordances = affordance;
      else if constexpr (std::is_same_v<Affordance, VectorAffordances>)
        affordances.vectorAffordances = affordance;
      else if constexpr (std::is_same_v<Affordance, MatrixAffordances>)
        affordances.matrixAffordances = affordance;
      else if constexpr (std::is_same_v<Affordance, AffordanceCollectionImpl>)
        affordances = affordance;
      return *this;
    }

    FErequirements &insertParameter(const FEParameter &key, ParameterTypeRaw &val) {
      parameter.insert_or_assign(key, val);
      return *this;
    }

    FErequirements &insertGlobalSolution(const FESolutions &key, SolutionVectorTypeRaw &sol) {
      sols.insert_or_assign(key, sol);
      return *this;
    }

    const SolutionVectorTypeRaw &getGlobalSolution(const FESolutions &key) const {
      try {
        if constexpr (std::is_same_v<SolutionVectorType, std::reference_wrapper<Eigen::VectorXd>>)
          return sols.at(key).get();
        else
          return sols.at(key);
      } catch (std::out_of_range &oor) {
        DUNE_THROW(Dune::RangeError,
                   std::string("Out of Range error: ") + std::string(oor.what()) + " in getGlobalSolution");
        abort();
      }
    }

    const ParameterTypeRaw &getParameter(FEParameter &&key) const { return parameter.at(key).get(); }

    template <FEAffordance Affordance>
    bool hasAffordance(Affordance &&affordance) const {
      if constexpr (std::is_same_v<Affordance, ScalarAffordances>)
        return affordances.scalarAffordances == affordance;
      else if constexpr (std::is_same_v<Affordance, VectorAffordances>)
        return affordances.vectorAffordances == affordance;
      else if constexpr (std::is_same_v<Affordance, MatrixAffordances>)
        return affordances.matrixAffordances == affordance;
      else if constexpr (std::is_same_v<Affordance, AffordanceCollectionImpl>)
        return affordances == affordance;
    }

  private:
    std::map<FESolutions, SolutionVectorType> sols;
    std::map<FEParameter, ParameterType> parameter;
    AffordanceCollectionImpl affordances;
  };

  template <typename ParameterType = double>
  class ResultTypeMap {
  public:
    using ResultArray = Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, 0, 3, 3>;
    void insertOrAssignResult(ResultType &&resultType, const ResultArray &resultArray) {
      results.insert_or_assign(resultType, resultArray);
    }

    ResultArray &getResult(ResultType &&resultType) { return results.at(resultType); }

  private:
    std::map<ResultType, ResultArray> results;
  };

  template <typename Type>
  concept ResultTypeConcept = std::is_same_v<Type, ResultType>;

  template <typename FErequirements = FErequirements<>>
  class ResultRequirements {
  public:
    using ParameterType         = typename FErequirements::ParameterType;
    using SolutionVectorType    = typename FErequirements::SolutionVectorType;
    using SolutionVectorTypeRaw = typename FErequirements::SolutionVectorTypeRaw;

    ResultRequirements(FErequirements &&req, std::set<ResultType> &&p_resType)
        : reqB{req}, resType(std::move(p_resType)) {}

    ResultRequirements() = default;
    bool isResultRequested(ResultType &&key) const { return resType.contains(key); }

    template <FEAffordance Affordance>
    ResultRequirements &addAffordance(Affordance &&affordance) {
      reqB.addAffordance(std::forward<Affordance>(affordance));
      return *this;
    }

    ResultRequirements &insertParameter(FEParameter &&key, ParameterType &val) {
      reqB.insertParameter(std::forward<FEParameter>(key), val);
      return *this;
    }

    ResultRequirements &insertGlobalSolution(FESolutions &&key, SolutionVectorTypeRaw &sol) {
      reqB.insertGlobalSolution(std::forward<FESolutions>(key), sol);
      return *this;
    }

    template <ResultTypeConcept... ResultTypes>
    ResultRequirements &addResultRequest(ResultTypes &&...keys) {
      resType.insert({std::move(keys)...});
      return *this;
    }

    const SolutionVectorTypeRaw &getGlobalSolution(FESolutions &&key) const {
      return reqB.getGlobalSolution(std::move(key));
    }

    const ParameterType &getParameter(FEParameter &&key) const { return reqB.getParameter(std::move(key)); }

    const FErequirements &getFERequirements() const { return reqB; }

  private:
    std::set<ResultType> resType;
    FErequirements reqB;
  };

}  // namespace Ikarus
