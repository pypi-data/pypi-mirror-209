#include <gtest/gtest.h>

#include "../include/dlplan/core.h"

using namespace dlplan::core;


TEST(DLPTests, RoleIdentity) {
    // Add predicates
    std::shared_ptr<VocabularyInfo> vocabulary = std::make_shared<VocabularyInfo>();
    Predicate p0 = vocabulary->add_predicate("concept", 1);
    std::shared_ptr<InstanceInfo> instance = std::make_shared<InstanceInfo>(vocabulary, 0);
    // Add state atoms
    Atom a0 = instance->add_atom("concept", {"A"});
    Atom a1 = instance->add_atom("concept", {"B"});

    State state(instance, {a0, a1}, 0);

    SyntacticElementFactory factory(vocabulary);
    DenotationsCaches caches;

    std::shared_ptr<const Role> role = factory.parse_role("r_identity(c_primitive(concept,0))");
    EXPECT_EQ(role->evaluate(state).to_sorted_vector(), IndexPair_Vec({{0,0},{1,1}}));
    EXPECT_EQ(role->evaluate(state, caches)->to_sorted_vector(), IndexPair_Vec({{0,0},{1,1}}));
    EXPECT_EQ(role->evaluate({state}, caches)->to_sorted_vector(), IndexPair_Vec({{0,0},{1,1}}));
}
