import numpy as np
from sklearn.metrics import pairwise_distances
import util
import pandas as pd
from hierarchy_node import HierarchyNode



def is_leaf(node, node_adj):
    return not node in node_adj.keys()



def trimming_algorithm(node, node_adj, trimmed, important):
    result = []
    if is_leaf(node, node_adj):
        return result, trimmed, important

    left = node_adj[node][0]
    right = node_adj[node][1]
    left_is_leaf = is_leaf(left, node_adj)
    right_is_leaf = is_leaf(right, node_adj)

    if left_is_leaf and right_is_leaf:
        trimmed.append(node)
        return result, trimmed, important

    if left_is_leaf:
        right_0 = node_adj[right][0]
        right_1 = node_adj[right][1]
        r0_leaf = is_leaf(right_0, node_adj)
        r1_leaf = is_leaf(right_1, node_adj)
        if r0_leaf and r1_leaf:
            result.append((right_0, right_1))
            important.append(node)
        else:
            r, t, i = trimming_algorithm(right, node_adj, trimmed, important)
            result.extend(r)
            important = i
            trimmed = t

    if right_is_leaf:
        left_0 = node_adj[left][0]
        left_1 = node_adj[left][1]
        l0_leaf = is_leaf(left_0, node_adj)
        l1_leaf = is_leaf(left_1, node_adj)
        if l0_leaf and l1_leaf:
            result.append((left_0, left_1))
            important.append(node)
        else:
            r, t, i = trimming_algorithm(left, node_adj, trimmed, important)
            result.extend(r)
            important = i
            trimmed = t

    if not (left_is_leaf or right_is_leaf):
        left_0 = node_adj[left][0]
        left_1 = node_adj[left][1]
        right_0 = node_adj[right][0]
        right_1 = node_adj[right][1]

        l0_leaf = is_leaf(left_0, node_adj)
        l1_leaf = is_leaf(left_1, node_adj)
        r0_leaf = is_leaf(right_0, node_adj)
        r1_leaf = is_leaf(right_1, node_adj)

        if l0_leaf and l1_leaf and r0_leaf and r1_leaf:
            result.extend([(left_0, left_1), (right_0, right_1)])
            important.append(node)
        else:
            r, t, i = trimming_algorithm(right, node_adj, trimmed, important)
            result.extend(r)
            important = i
            trimmed = t
            r, t, i = trimming_algorithm(left, node_adj, trimmed, important)
            result.extend(r)
            important = i
            trimmed = t

    return result, trimmed, important


def trim_tree(node, node_adj, trimmed):
    remaining = []
    if is_leaf(node, node_adj):
        remaining.append(node)
        return remaining, trimmed

    left = node_adj[node][0]
    right = node_adj[node][1]
    left_is_leaf = is_leaf(left, node_adj)
    right_is_leaf = is_leaf(right, node_adj)

    if left_is_leaf and right_is_leaf:
        trimmed.append(node)
        return remaining, trimmed

    if left_is_leaf:
        right_0 = node_adj[right][0]
        right_1 = node_adj[right][1]
        r0_leaf = is_leaf(right_0, node_adj)
        r1_leaf = is_leaf(right_1, node_adj)
        if r0_leaf and r1_leaf:
            remaining.extend([right_0, right_1])
        else:
            remaining.append(left)
            r, t = trim_tree(right, node_adj, trimmed)
            remaining.extend(r)

    if right_is_leaf:
        left_0 = node_adj[left][0]
        left_1 = node_adj[left][1]
        l0_leaf = is_leaf(left_0, node_adj)
        l1_leaf = is_leaf(left_1, node_adj)
        if l0_leaf and l1_leaf:
            remaining.extend([left_0, left_1])
        else:
            remaining.append(right)
            r, t = trim_tree(left, node_adj, trimmed)
            remaining.extend(r)

    if not (left_is_leaf or right_is_leaf):
        left_0 = node_adj[left][0]
        left_1 = node_adj[left][1]
        right_0 = node_adj[right][0]
        right_1 = node_adj[right][1]

        l0_leaf = is_leaf(left_0, node_adj)
        l1_leaf = is_leaf(left_1, node_adj)
        r0_leaf = is_leaf(right_0, node_adj)
        r1_leaf = is_leaf(right_1, node_adj)

        if l0_leaf and l1_leaf and r0_leaf and r1_leaf:
            remaining.extend([left_0, left_1, right_0, right_1])
        else:
            r, t = trim_tree(right, node_adj, trimmed)
            remaining.extend(r)
            trimmed = t
            r, t = trim_tree(left, node_adj, trimmed)
            remaining.extend(r)
            trimmed = t

    return remaining, trimmed


def minimize_maximum_distance_seed_selection(seeds, dist_matrix):
    result = []
    for pair in seeds:
        s1, s2 = pair[0], pair[1]
        m1, m2 = dist_matrix[s1, :], dist_matrix[s2, :]
        measure1 = np.max(m1)
        measure2 = np.max(m2)
        if measure1 < measure2:
            result.append(s1)
        elif measure1 > measure2:
            result.append(s2)
        else:
            result.append(np.min([s1, s2]))
    return result


def minimize_average_distance_seed_selection(seeds, dist_matrix):
    result = []
    for pair in seeds:
        s1, s2 = pair[0], pair[1]
        m1, m2 = dist_matrix[s1, :], dist_matrix[s2, :]
        measure1 = np.mean(m1)
        measure2 = np.mean(m2)
        if measure1 < measure2:
            result.append(s1)
        elif measure1 > measure2:
            result.append(s2)
        else:
            result.append(np.min([s1, s2]))
    return result


def minimize_average_distance_to_trimmed_tree_seed_selection(seeds, embs, adjacency, trimmed):
    new_embs, new_to_old, old_to_new = remove_trimmed_embs(embs, adjacency, trimmed)
    new_seeds = []
    for pair in seeds:
        s1, s2 = pair
        n1, n2 = old_to_new[s1], old_to_new[s2]
        new_seeds.append((n1, n2))
    D = pairwise_distances(new_embs, metric='cosine')
    result = minimize_average_distance_seed_selection(new_seeds, D)
    result_original = []
    for r in result:
        result_original.append(new_to_old[r])

    return result_original


def get_all_salient_primary_pairs(salient_nodes, adjacency):
    n_leaves = np.min(list(adjacency.keys()))
    c = []
    for salient in salient_nodes:
        r, l = adjacency[salient]
        if r >= n_leaves: c.append(r)
        if l >= n_leaves: c.append(l)
    return c


def get_hierarchy_summary(embs, sents):
    hn = HierarchyNode(embs)
    node_persistence = hn.calculate_persistence()
    root = np.max(list(hn.h_nodes_adj.keys()))
    seeds, trimmed, important = trimming_algorithm(root, hn.h_nodes_adj, [], [])
    if len(seeds) > 5:
        candidates = get_all_salient_primary_pairs(important, hn.h_nodes_adj)
        cp = [node_persistence[node_persistence['id'] == c]['persistence'].iloc[0] for c in candidates]
        candidate_persistence = pd.DataFrame({'id': candidates, 'persistence': cp})
        candidate_persistence = candidate_persistence.sort_values('persistence', ascending=False)
        best_candidates = candidate_persistence.head(5)['id'].tolist()
        seeds = []
        for bc in best_candidates:
            r, l = hn.h_nodes_adj[bc]
            seeds.append([r, l])

    summary = np.sort(minimize_average_distance_seed_selection(seeds, hn.distance_matrix))
    summary_text = [sents[x] for x in summary]
    return summary_text, hn.h_nodes_adj, trimmed, important, node_persistence


def get_hierarchy_summary_ids(embs):
    hn = HierarchyNode(embs)
    node_persistence = hn.calculate_persistence()
    root = np.max(list(hn.h_nodes_adj.keys()))
    seeds, trimmed, important = trimming_algorithm(root, hn.h_nodes_adj, [], [])
    trimmed_c = trimmed.copy()
    if len(seeds) > 5:
        candidates = get_all_salient_primary_pairs(important, hn.h_nodes_adj)
        cp = [node_persistence[node_persistence['id'] == c]['persistence'].iloc[0] for c in candidates]
        candidate_persistence = pd.DataFrame({'id': candidates, 'persistence': cp})
        candidate_persistence = candidate_persistence.sort_values('persistence', ascending=False)
        best_candidates = candidate_persistence.head(5)['id'].tolist()
        seeds = []
        for bc in best_candidates:
            r, l = hn.h_nodes_adj[bc]
            seeds.append([r, l])
            
    summary_untrimmed = np.sort(
        minimize_average_distance_to_trimmed_tree_seed_selection(seeds, embs, hn.h_nodes_adj, trimmed_c))
    return summary_untrimmed, trimmed, important


def get_k_center_summary(summary_length, embs, sents):
    summary = util.k_centers(util.pairwise_distances(embs, metric='cosine'), k=summary_length)
    summary = np.sort(list(summary))
    summary_text = [sents[x] for x in summary]
    return summary_text


def get_k_center_summary_after_trimming(summary_length, embs, sents, adjacency, trimmed):
    new_embs, new_to_old, old_to_new = remove_trimmed_embs(embs, adjacency, trimmed)
    ids = get_k_center_summary_ids(summary_length, new_embs)
    summary = []
    for id in ids:
        summary.append(new_to_old[id])
    summary_text = [sents[x] for x in summary]
    return summary_text


def remove_trimmed_embs(embs, adjacency, trimmed):
    trimmed_leaves = []
    for t in trimmed:
        trimmed_leaves.extend(adjacency[t])
    new_embs = np.empty((0, embs.shape[1]))
    new_to_old = {}
    old_to_new = {}
    new_id = 0
    for i in range(0, embs.shape[0]):
        if i in trimmed_leaves:
            continue
        new_embs = np.vstack((new_embs, embs[i]))
        new_to_old[new_id] = i
        old_to_new[i] = new_id
        new_id += 1
    return new_embs, new_to_old, old_to_new


def get_k_center_summary_ids(summary_length, embs):
    summary = util.k_centers(util.pairwise_distances(embs, metric='cosine'), k=summary_length)
    return summary


