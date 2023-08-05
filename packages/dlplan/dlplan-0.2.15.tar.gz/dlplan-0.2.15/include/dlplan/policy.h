#ifndef DLPLAN_INCLUDE_DLPLAN_POLICY_H_
#define DLPLAN_INCLUDE_DLPLAN_POLICY_H_

#include "core.h"
#include "utils/pimpl.h"

#include <unordered_set>
#include <memory>
#include <set>
#include <string>
#include <vector>


/**
 * Forward declarations and usings
 */
namespace dlplan::policy {
    class PolicyBuilder;
    class PolicyBuilderImpl;
    class PolicyReaderImpl;
    class PolicyWriterImpl;
    class BaseCondition;
    class BaseEffect;
    class Rule;
    class Policy;

    using Booleans = std::set<std::shared_ptr<const dlplan::core::Boolean>>;
    using Numericals = std::set<std::shared_ptr<const dlplan::core::Numerical>>;

    using Conditions = std::set<std::shared_ptr<const BaseCondition>>;
    using Effects = std::set<std::shared_ptr<const BaseEffect>>;
    using Rules = std::set<std::shared_ptr<const Rule>>;

    using Policies = std::set<std::shared_ptr<const Policy>>;
}


namespace dlplan::policy {
/**
 * All different kinds of conditions.
 */
class BaseCondition : public dlplan::utils::Cachable {
private:
    std::shared_ptr<const core::BaseElement> m_base_feature;
    int m_index;

protected:
    BaseCondition(std::shared_ptr<const core::BaseElement> base_feature);

public:
    // Condition is not copieable because it must live in the cache.
    BaseCondition(const BaseCondition& other) = delete;
    BaseCondition& operator=(const BaseCondition& other) = delete;
    BaseCondition(BaseCondition&& other) = delete;
    BaseCondition& operator=(BaseCondition&& other) = delete;
    virtual ~BaseCondition();

    virtual bool evaluate(const core::State& source_state) const = 0;
    virtual bool evaluate(const core::State& source_state, core::DenotationsCaches& caches) const = 0;

    virtual std::string compute_repr() const = 0;

    virtual std::string str() const = 0;

    /**
     * Adds the condition to the policy builder and returns it
     */
    virtual std::shared_ptr<const BaseCondition> copy_to_builder(PolicyBuilder& policy_builder) const = 0;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    std::shared_ptr<const core::BaseElement> get_base_feature() const;
    virtual std::shared_ptr<const core::Boolean> get_boolean() const = 0;
    virtual std::shared_ptr<const core::Numerical> get_numerical() const = 0;
    int get_index() const;
};


/**
 * All different kinds of effects.
 */
class BaseEffect : public dlplan::utils::Cachable {
private:
    std::shared_ptr<const core::BaseElement> m_base_feature;
    int m_index;

protected:
    BaseEffect(std::shared_ptr<const core::BaseElement> base_feature);

public:
    // Effect is not copieable because it must live in the cache.
    BaseEffect(const BaseEffect& other) = delete;
    BaseEffect& operator=(const BaseEffect& other) = delete;
    BaseEffect(BaseEffect&& other) = delete;
    BaseEffect& operator=(BaseEffect&& other) = delete;
    virtual ~BaseEffect();

    virtual bool evaluate(const core::State& source_state, const core::State& target_state) const = 0;
    virtual bool evaluate(const core::State& source_state, const core::State& target_state, core::DenotationsCaches& caches) const = 0;

    virtual std::string compute_repr() const = 0;

    virtual std::string str() const = 0;

    /**
     * Adds the effect to the policy builder and returns it
     */
    virtual std::shared_ptr<const BaseEffect> copy_to_builder(PolicyBuilder& policy_builder) const = 0;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    int get_index() const;
    std::shared_ptr<const core::BaseElement> get_base_feature() const;
    virtual std::shared_ptr<const core::Boolean> get_boolean() const = 0;
    virtual std::shared_ptr<const core::Numerical> get_numerical() const = 0;
};


/**
 * A rule over Boolean and numerical features has form C -> E
 * where C is set of feature conditions and E is set of feature effects
 */
class Rule : public dlplan::utils::Cachable {
private:
    Conditions m_conditions;
    Effects m_effects;
    int m_index;

private:
    Rule(Conditions&& conditions, Effects&& effects);
    friend class PolicyBuilderImpl;

public:
    // Rule is not copieable because it must live in the cache.
    Rule(const Rule& other) = delete;
    Rule& operator=(const Rule& other) = delete;
    Rule(Rule&& other) = delete;
    Rule& operator=(Rule&& other) = delete;
    ~Rule();

    bool evaluate_conditions(const core::State& source_state) const;
    bool evaluate_conditions(const core::State& source_state, core::DenotationsCaches& caches) const;
    bool evaluate_effects(const core::State& source_state, const core::State& target_state) const;
    bool evaluate_effects(const core::State& source_state, const core::State& target_state, core::DenotationsCaches& caches) const;

    std::string compute_repr() const;

    std::string str() const;

    /**
     * Adds the rule to the policy builder and returns it
     */
    std::shared_ptr<const Rule> copy_to_builder(PolicyBuilder& policy_builder) const;

    /**
     * Setters.
     */
    void set_index(int index);

    /**
     * Getters.
     */
    int get_index() const;
    const Conditions& get_conditions() const;
    const Effects& get_effects() const;
};


/**
 * A policy is a set of rules over Boolean and numerical features.
 */
class Policy : public dlplan::utils::Cachable {
private:
    Booleans m_booleans;
    Numericals m_numericals;
    Rules m_rules;
    int m_index;

private:
    explicit Policy(Rules&& rules);
    friend class PolicyBuilderImpl;

public:
    Policy();
    Policy(const Policy& other);
    Policy& operator=(const Policy& other);
    Policy(Policy&& other);
    Policy& operator=(Policy&& other);
    ~Policy();

    /**
     * Approach 1: naive approach to evaluate (s,s')
     */
    std::shared_ptr<const Rule> evaluate_lazy(const core::State& source_state, const core::State& target_state) const;
    std::shared_ptr<const Rule> evaluate_lazy(const core::State& source_state, const core::State& target_state, core::DenotationsCaches& caches) const;

    /**
     * Approach 2: optimized approach for evaluating pairs with similar source state s, i.e., (s,s1), (s,s2), ..., (s,sn)
     */
    std::vector<std::shared_ptr<const Rule>> evaluate_conditions_eager(const core::State& source_state) const;
    std::vector<std::shared_ptr<const Rule>> evaluate_conditions_eager(const core::State& source_state, core::DenotationsCaches& caches) const;
    std::shared_ptr<const Rule> evaluate_effects_lazy(const core::State& source_state, const core::State& target_state, const std::vector<std::shared_ptr<const Rule>>& rules) const;
    std::shared_ptr<const Rule> evaluate_effects_lazy(const core::State& source_state, const core::State& target_state, const std::vector<std::shared_ptr<const Rule>>& rules, core::DenotationsCaches& caches) const;

    /**
     * Returns a canonical string representation that can be parsed.
     */
    std::string compute_repr() const;

    /**
     * Returns a more readable string representation that is not necessarily canonical.
     */
    std::string str() const;

    /**
     * Adds the rule to the policy builder and returns it
     */
    std::shared_ptr<const Policy> copy_to_builder(PolicyBuilder& policy_builder) const;

    /**
     * Setters.
     */
    void set_index(int index);
    /**
     * Getters.
     */
    int get_index() const;
    const Booleans& get_booleans() const;
    const Numericals& get_numericals() const;
    const Rules& get_rules() const;
};

/**
 * PolicyBuilder for the construction of a forest of policies.
*/
class PolicyBuilder {
private:
    dlplan::utils::pimpl<PolicyBuilderImpl> m_pImpl;

public:
    PolicyBuilder();
    PolicyBuilder(const PolicyBuilder& other);
    PolicyBuilder& operator=(const PolicyBuilder& other);
    PolicyBuilder(PolicyBuilder&& other);
    PolicyBuilder& operator=(PolicyBuilder&& other);
    ~PolicyBuilder();

    /**
     * Uniquely adds a condition (resp. effect) and returns it.
     */
    std::shared_ptr<const BaseCondition> add_pos_condition(const std::shared_ptr<const core::Boolean>& boolean);
    std::shared_ptr<const BaseCondition> add_neg_condition(const std::shared_ptr<const core::Boolean>& boolean);
    std::shared_ptr<const BaseCondition> add_gt_condition(const std::shared_ptr<const core::Numerical>& numerical);
    std::shared_ptr<const BaseCondition> add_eq_condition(const std::shared_ptr<const core::Numerical>& numerical);
    std::shared_ptr<const BaseEffect> add_pos_effect(const std::shared_ptr<const core::Boolean>& boolean);
    std::shared_ptr<const BaseEffect> add_neg_effect(const std::shared_ptr<const core::Boolean>& boolean);
    std::shared_ptr<const BaseEffect> add_bot_effect(const std::shared_ptr<const core::Boolean>& boolean);
    std::shared_ptr<const BaseEffect> add_inc_effect(const std::shared_ptr<const core::Numerical>& numerical);
    std::shared_ptr<const BaseEffect> add_dec_effect(const std::shared_ptr<const core::Numerical>& numerical);
    std::shared_ptr<const BaseEffect> add_bot_effect(const std::shared_ptr<const core::Numerical>& numerical);

    /**
     * Uniquely adds a rule and returns it.
     */
    std::shared_ptr<const Rule> add_rule(
        std::set<std::shared_ptr<const BaseCondition>>&& conditions,
        std::set<std::shared_ptr<const BaseEffect>>&& effects);

    /**
     * Uniquely adds a policy and returns it.
     */
    std::shared_ptr<const Policy> add_policy(
        std::set<std::shared_ptr<const Rule>>&& rules);
};


/**
 * PolicyMinimizer provides methods to minimize the number of rules in a policy.
 */
class PolicyMinimizer {
public:
    PolicyMinimizer();
    PolicyMinimizer(const PolicyMinimizer& other);
    PolicyMinimizer& operator=(const PolicyMinimizer& other);
    PolicyMinimizer(PolicyMinimizer&& other);
    PolicyMinimizer& operator=(PolicyMinimizer&& other);
    ~PolicyMinimizer();

    std::shared_ptr<const Policy> minimize(const std::shared_ptr<const Policy>& policy, PolicyBuilder& builder) const;
    std::shared_ptr<const Policy> minimize(const std::shared_ptr<const Policy>& policy, const core::StatePairs& true_state_pairs, const core::StatePairs& false_state_pairs, PolicyBuilder& builder) const;
};


/**
 * PolicyReader for reading general policy from bytestream.
 */
class PolicyReader {
private:
    dlplan::utils::pimpl<PolicyReaderImpl> m_pImpl;

public:
    PolicyReader();
    PolicyReader(const PolicyReader& other);
    PolicyReader& operator=(const PolicyReader& other);
    PolicyReader(PolicyReader&& other);
    PolicyReader& operator=(PolicyReader&& other);
    ~PolicyReader();

    std::shared_ptr<const Policy> read(const std::string& data, PolicyBuilder& builder, core::SyntacticElementFactory& factory) const;
};

/**
 * PolicyWriter for writing general policy to bytestream.
 */
class PolicyWriter {
    dlplan::utils::pimpl<PolicyWriterImpl> m_pImpl;

public:
    PolicyWriter();
    PolicyWriter(const PolicyWriter& other);
    PolicyWriter& operator=(const PolicyWriter& other);
    PolicyWriter(PolicyWriter&& other);
    PolicyWriter& operator=(PolicyWriter&& other);
    ~PolicyWriter();

    std::string write(const Policy& policy) const;
};

}

#endif