#include "../../include/dlplan/core.h"

#include "element_factory.h"

#include "../../include/dlplan/utils/hashing.h"

#include <cassert>
#include <iostream>
#include <algorithm>
#include <sstream>


namespace std {
    size_t hash<dlplan::core::State>::operator()(const dlplan::core::State& state) const noexcept {
        return state.hash();
    }
    size_t hash<unique_ptr<dlplan::core::ConceptDenotation>>::operator()(const unique_ptr<dlplan::core::ConceptDenotation>& denotation) const noexcept {
        return denotation->hash();
    }
    size_t hash<unique_ptr<dlplan::core::RoleDenotation>>::operator()(const unique_ptr<dlplan::core::RoleDenotation>& denotation) const noexcept {
        return denotation->hash();
    }
    size_t hash<unique_ptr<dlplan::core::ConceptDenotations>>::operator()(const unique_ptr<dlplan::core::ConceptDenotations>& denotations) const noexcept {
        size_t seed = 0;
        for (const auto denot_ptr : *denotations) {
            dlplan::utils::hash_combine(seed, denot_ptr);
        }
        return seed;
    }
    size_t hash<unique_ptr<dlplan::core::RoleDenotations>>::operator()(const unique_ptr<dlplan::core::RoleDenotations>& denotations) const noexcept {
        size_t seed = 0;
        for (const auto denot_ptr : *denotations) {
            dlplan::utils::hash_combine(seed, denot_ptr);
        }
        return seed;
    }
    size_t hash<unique_ptr<dlplan::core::BooleanDenotations>>::operator()(const unique_ptr<dlplan::core::BooleanDenotations>& denotations) const noexcept {
        return hash<dlplan::core::BooleanDenotations>()(*denotations);
    }
    size_t hash<unique_ptr<dlplan::core::NumericalDenotations>>::operator()(const unique_ptr<dlplan::core::NumericalDenotations>& denotations) const noexcept {
        return hash<dlplan::core::NumericalDenotations>()(*denotations);
    }
    size_t hash<vector<unsigned>>::operator()(const vector<unsigned>& data) const noexcept {
        size_t seed = data.size();
        for (unsigned value : data) {
            dlplan::utils::hash_combine(seed, value);
        }
        return seed;
    }
    size_t hash<vector<int>>::operator()(const vector<int>& data) const noexcept {
        size_t seed = data.size();
        for (int value : data) {
            dlplan::utils::hash_combine(seed, value);
        }
        return seed;
    }
    size_t hash<std::array<int, 2>>::operator()(const std::array<int, 2>& data) const noexcept {
        size_t seed = data.size();
        for (int value : data) {
            dlplan::utils::hash_combine(seed, value);
        }
        return seed;
    }
    size_t hash<std::array<int, 3>>::operator()(const std::array<int, 3>& data) const noexcept {
        size_t seed = data.size();
        for (int value : data) {
            dlplan::utils::hash_combine(seed, value);
        }
        return seed;
    }
}


namespace dlplan::core {

ConceptDenotation::ConceptDenotation(int num_objects)
    : m_num_objects(num_objects), m_data(utils::DynamicBitset<unsigned>(num_objects)) { }

ConceptDenotation::ConceptDenotation(const ConceptDenotation& other) = default;

ConceptDenotation& ConceptDenotation::operator=(const ConceptDenotation& other) = default;

ConceptDenotation::ConceptDenotation(ConceptDenotation&& other) = default;

ConceptDenotation& ConceptDenotation::operator=(ConceptDenotation&& other) = default;

ConceptDenotation::~ConceptDenotation() = default;

void ConceptDenotation::const_iterator::seek_next() {
    while (++m_index < m_num_objects) {
        if (m_data.test(m_index)) break;
    }
}

ConceptDenotation::const_iterator::const_iterator(
    ConceptDenotation::const_iterator::const_reference data, int num_objects, bool end)
    : m_data(data), m_num_objects(num_objects), m_index(end ? num_objects : -1) {
    if (!end) seek_next();
}

bool ConceptDenotation::const_iterator::operator!=(const const_iterator& other) const {
    return !(*this == other);
}

bool ConceptDenotation::const_iterator::operator==(const const_iterator& other) const {
    return ((m_index == other.m_index) && (&m_data == &other.m_data));
}

const int& ConceptDenotation::const_iterator::operator*() const {
    return m_index;
}

ConceptDenotation::const_iterator ConceptDenotation::const_iterator::operator++(int) {
    ConceptDenotation::const_iterator prev = *this;
    seek_next();
    return prev;
}

ConceptDenotation::const_iterator& ConceptDenotation::const_iterator::operator++() {
    seek_next();
    return *this;
}

bool ConceptDenotation::operator==(const ConceptDenotation& other) const {
    if (this != &other) {
        return this->m_data == other.m_data;
    }
    return true;
}

bool ConceptDenotation::operator!=(const ConceptDenotation& other) const {
    return !(*this == other);
}

ConceptDenotation& ConceptDenotation::operator&=(const ConceptDenotation& other) {
    m_data &= other.m_data;
    return *this;
}

ConceptDenotation& ConceptDenotation::operator|=(const ConceptDenotation& other) {
    m_data |= other.m_data;
    return *this;
}

ConceptDenotation& ConceptDenotation::operator-=(const ConceptDenotation& other) {
    m_data -= other.m_data;
    return *this;
}

ConceptDenotation& ConceptDenotation::operator~() {
    ~m_data;
    return *this;
}

ConceptDenotation::const_iterator ConceptDenotation::begin() const {
    return ConceptDenotation::const_iterator(m_data, m_num_objects);
}

ConceptDenotation::const_iterator ConceptDenotation::end() const {
    return ConceptDenotation::const_iterator(m_data, m_num_objects, true);
}

bool ConceptDenotation::contains(int value) const {
    assert(value >= 0 && value < m_num_objects);
    return m_data.test(value);
}

void ConceptDenotation::set() {
    m_data.set();
}

void ConceptDenotation::insert(int value) {
    assert(value >= 0 && value < m_num_objects);
    m_data.set(value);
}

void ConceptDenotation::erase(int value) {
    assert(value >= 0 && value < m_num_objects);
    m_data.reset(value);
}

int ConceptDenotation::size() const {
    return m_data.count();
}

bool ConceptDenotation::empty() const {
    return m_data.none();
}

bool ConceptDenotation::intersects(const ConceptDenotation& other) const {
    return m_data.intersects(other.m_data);
}

bool ConceptDenotation::is_subset_of(const ConceptDenotation& other) const {
    return m_data.is_subset_of(other.m_data);
}

std::vector<int> ConceptDenotation::to_sorted_vector() const {
    std::vector<int> result;
    result.reserve(m_num_objects);
    for (int i = 0; i < m_num_objects; ++i) {
        if (m_data.test(i)) result.push_back(i);
    }
    result.shrink_to_fit();
    return result;
}

std::size_t ConceptDenotation::hash() const {
    return std::hash<std::vector<unsigned>>()(m_data.get_blocks());
}

std::string ConceptDenotation::str() const {
    std::stringstream ss;
    ss << "{";
    std::vector<int> object_idxs = to_sorted_vector();
    for (int i : object_idxs) {
        ss << i;
        if (i != object_idxs.back()) ss << ", ";
    }
    ss << "}";
    return ss.str();
}

int ConceptDenotation::get_num_objects() const {
    return m_num_objects;
}


RoleDenotation::RoleDenotation(int num_objects)
    : m_num_objects(num_objects), m_data(utils::DynamicBitset<unsigned>(num_objects * num_objects)) { }

RoleDenotation::RoleDenotation(const RoleDenotation& other) = default;

RoleDenotation& RoleDenotation::operator=(const RoleDenotation& other) = default;

RoleDenotation::RoleDenotation(RoleDenotation&& other) = default;

RoleDenotation& RoleDenotation::operator=(RoleDenotation&& other) = default;

RoleDenotation::~RoleDenotation() = default;

void RoleDenotation::const_iterator::seek_next() {
    int& i = m_indices.first;
    int& j = m_indices.second;
    int offset = i * m_num_objects;
    while (i < m_num_objects) {
        ++j;
        if (j == m_num_objects) {  // end of row is reached
            ++i;
            offset += m_num_objects;
            j = 0;
            if (i == m_num_objects) break;  // reached last row
        }
        if (m_data.test(offset + j)) break;
    }
    assert(offset + j <= static_cast<int>(m_data.size()));
}

RoleDenotation::const_iterator::const_iterator(const_reference data, int num_objects, bool end)
    : m_data(data), m_num_objects(num_objects), m_indices(end ? std::pair<size_t, size_t>(num_objects, 0) : std::pair<size_t, size_t>(0, -1)) {
    if (!end) seek_next();
}

bool RoleDenotation::const_iterator::operator!=(const const_iterator& other) const {
    return !(*this == other);
}

bool RoleDenotation::const_iterator::operator==(const const_iterator& other) const {
    return ((m_indices == other.m_indices) && (&m_data == &other.m_data));
}

const std::pair<int, int>& RoleDenotation::const_iterator::operator*() const {
    return m_indices;
}

std::pair<int, int>* RoleDenotation::const_iterator::operator->() {
    return &m_indices;
}

RoleDenotation::const_iterator RoleDenotation::const_iterator::operator++(int) {
    RoleDenotation::const_iterator prev = *this;
    seek_next();
    return prev;
}

RoleDenotation::const_iterator& RoleDenotation::const_iterator::operator++() {
    seek_next();
    return *this;
}

bool RoleDenotation::operator==(const RoleDenotation& other) const {
    if (this != &other) {
        return this->m_data == other.m_data;
    }
    return true;
}

bool RoleDenotation::operator!=(const RoleDenotation& other) const {
    return !(*this == other);
}

RoleDenotation& RoleDenotation::operator&=(const RoleDenotation& other) {
    m_data &= other.m_data;
    return *this;
}

RoleDenotation& RoleDenotation::operator|=(const RoleDenotation& other) {
    m_data |= other.m_data;
    return *this;
}

RoleDenotation& RoleDenotation::operator-=(const RoleDenotation& other) {
    m_data -= other.m_data;
    return *this;
}

RoleDenotation& RoleDenotation::operator~() {
    ~m_data;
    return *this;
}

RoleDenotation::const_iterator RoleDenotation::begin() const {
    return RoleDenotation::const_iterator(m_data, m_num_objects);
}

RoleDenotation::const_iterator RoleDenotation::end() const {
    return RoleDenotation::const_iterator(m_data, m_num_objects, true);
}

void RoleDenotation::set() {
    m_data.set();
}

bool RoleDenotation::contains(const std::pair<int, int>& value) const {
    return m_data.test(value.first * m_num_objects + value.second);
}

void RoleDenotation::insert(const std::pair<int, int>& value) {
    return m_data.set(value.first * m_num_objects + value.second);
}

void RoleDenotation::erase(const std::pair<int, int>& value) {
    return m_data.reset(value.first * m_num_objects + value.second);
}

int RoleDenotation::size() const {
    return m_data.count();
}

bool RoleDenotation::empty() const {
    return m_data.none();
}

bool RoleDenotation::intersects(const RoleDenotation& other) const {
    return m_data.intersects(other.m_data);
}

bool RoleDenotation::is_subset_of(const RoleDenotation& other) const {
    return m_data.is_subset_of(other.m_data);
}

std::vector<std::pair<int, int>> RoleDenotation::to_sorted_vector() const {
    std::vector<std::pair<int, int>> result;
    result.reserve(m_num_objects * m_num_objects);
    for (int i = 0; i < m_num_objects; ++i) {
        for (int j = 0; j < m_num_objects; ++j) {
            if (m_data.test(i * m_num_objects + j)) {
                result.emplace_back(i, j);
            }
        }
    }
    result.shrink_to_fit();
    return result;
}

std::size_t RoleDenotation::hash() const {
    return std::hash<std::vector<unsigned>>()(m_data.get_blocks());
}

std::string RoleDenotation::str() const {
    std::stringstream ss;
    ss << "{";
    std::vector<std::pair<int, int>> object_pair_idxs = to_sorted_vector();
    for (const auto& p : object_pair_idxs) {
        ss << "(" << p.first << ", " << p.second << ")";
        if (p != object_pair_idxs.back()) ss << ", ";
    }
    ss << "}";
    return ss.str();
}

int RoleDenotation::get_num_objects() const {
    return m_num_objects;
}


SyntacticElementFactory::SyntacticElementFactory(std::shared_ptr<const VocabularyInfo> vocabulary_info) : m_pImpl(SyntacticElementFactoryImpl(vocabulary_info)) { }

SyntacticElementFactory::SyntacticElementFactory(const SyntacticElementFactory& other) : m_pImpl(*other.m_pImpl) { }

SyntacticElementFactory& SyntacticElementFactory::operator=(const SyntacticElementFactory& other) {
    if (this != &other) {
        *m_pImpl = *other.m_pImpl;
    }
    return *this;
}

SyntacticElementFactory::SyntacticElementFactory(SyntacticElementFactory&& other)
    : m_pImpl(std::move(*other.m_pImpl)) { }

SyntacticElementFactory& SyntacticElementFactory::operator=(SyntacticElementFactory&& other) {
    if (this != &other) {
        std::swap(*m_pImpl, *other.m_pImpl);
    }
    return *this;
}

SyntacticElementFactory::~SyntacticElementFactory() = default;

std::shared_ptr<const VocabularyInfo> SyntacticElementFactory::get_vocabulary_info() const {
    return m_pImpl->get_vocabulary_info();
}

std::shared_ptr<const Concept> SyntacticElementFactory::parse_concept(const std::string &description) {
    return m_pImpl->parse_concept(description);
}

std::shared_ptr<const Role>SyntacticElementFactory::parse_role(const std::string &description) {
    return m_pImpl->parse_role(description);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::parse_numerical(const std::string &description) {
    return m_pImpl->parse_numerical(description);
}

std::shared_ptr<const Boolean>SyntacticElementFactory::parse_boolean(const std::string &description) {
    return m_pImpl->parse_boolean(description);
}


std::shared_ptr<const Boolean>SyntacticElementFactory::make_empty_boolean(const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_empty_boolean(concept);
}

std::shared_ptr<const Boolean>SyntacticElementFactory::make_empty_boolean(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_empty_boolean(role);
}

std::shared_ptr<const Boolean>SyntacticElementFactory::make_inclusion_boolean(const std::shared_ptr<const Concept>& concept_left, const std::shared_ptr<const Concept>& concept_right) {
    return m_pImpl->make_inclusion_boolean(concept_left, concept_right);
}

std::shared_ptr<const Boolean>SyntacticElementFactory::make_inclusion_boolean(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_inclusion_boolean(role_left, role_right);
}

std::shared_ptr<const Boolean>SyntacticElementFactory::make_nullary_boolean(const Predicate& predicate) {
    return m_pImpl->make_nullary_boolean(predicate);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_all_concept(const std::shared_ptr<const Role>& role, const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_all_concept(role, concept);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_and_concept(const std::shared_ptr<const Concept>& concept_left, const std::shared_ptr<const Concept>& concept_right) {
    return m_pImpl->make_and_concept(concept_left, concept_right);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_bot_concept() {
    return m_pImpl->make_bot_concept();
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_diff_concept(const std::shared_ptr<const Concept>& concept_left, const std::shared_ptr<const Concept>& concept_right) {
    return m_pImpl->make_diff_concept(concept_left, concept_right);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_equal_concept(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_equal_concept(role_left, role_right);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_not_concept(const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_not_concept(concept);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_one_of_concept(const Constant& constant) {
    return m_pImpl->make_one_of_concept(constant);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_or_concept(const std::shared_ptr<const Concept>& concept_left, const std::shared_ptr<const Concept>& concept_right) {
    return m_pImpl->make_or_concept(concept_left, concept_right);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_projection_concept(const std::shared_ptr<const Role>& role, int pos) {
    return m_pImpl->make_projection_concept(role, pos);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_primitive_concept(const Predicate& predicate, int pos) {
    return m_pImpl->make_primitive_concept(predicate, pos);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_some_concept(const std::shared_ptr<const Role>& role, const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_some_concept(role, concept);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_subset_concept(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_subset_concept(role_left, role_right);
}

std::shared_ptr<const Concept>SyntacticElementFactory::make_top_concept() {
    return m_pImpl->make_top_concept();
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_concept_distance_numerical(const std::shared_ptr<const Concept>& concept_from, const std::shared_ptr<const Role>& role, const std::shared_ptr<const Concept>& concept_to) {
    return m_pImpl->make_concept_distance_numerical(concept_from, role, concept_to);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_count_numerical(const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_count_numerical(concept);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_count_numerical(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_count_numerical(role);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_role_distance_numerical(const std::shared_ptr<const Role>& role_from, const std::shared_ptr<const Role>& role, const std::shared_ptr<const Role>& role_to) {
    return m_pImpl->make_role_distance_numerical(role_from, role, role_to);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_sum_concept_distance_numerical(const std::shared_ptr<const Concept>& concept_from, const std::shared_ptr<const Role>& role, const std::shared_ptr<const Concept>& concept_to) {
    return m_pImpl->make_sum_concept_distance_numerical(concept_from, role, concept_to);
}

std::shared_ptr<const Numerical>SyntacticElementFactory::make_sum_role_distance_numerical(const std::shared_ptr<const Role>& role_from, const std::shared_ptr<const Role>& role, const std::shared_ptr<const Role>& role_to) {
    return m_pImpl->make_sum_role_distance_numerical(role_from, role, role_to);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_and_role(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_and_role(role_left, role_right);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_compose_role(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_compose_role(role_left, role_right);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_diff_role(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_diff_role(role_left, role_right);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_identity_role(const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_identity_role(concept);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_inverse_role(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_inverse_role(role);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_not_role(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_not_role(role);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_or_role(const std::shared_ptr<const Role>& role_left, const std::shared_ptr<const Role>& role_right) {
    return m_pImpl->make_or_role(role_left, role_right);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_primitive_role(const Predicate& predicate, int pos_1, int pos_2) {
    return m_pImpl->make_primitive_role(predicate, pos_1, pos_2);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_restrict_role(const std::shared_ptr<const Role>& role, const std::shared_ptr<const Concept>& concept) {
    return m_pImpl->make_restrict_role(role, concept);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_top_role() {
    return m_pImpl->make_top_role();
}

std::shared_ptr<const Role>SyntacticElementFactory::make_transitive_closure(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_transitive_closure(role);
}

std::shared_ptr<const Role>SyntacticElementFactory::make_transitive_reflexive_closure(const std::shared_ptr<const Role>& role) {
    return m_pImpl->make_transitive_reflexive_closure(role);
}

}
