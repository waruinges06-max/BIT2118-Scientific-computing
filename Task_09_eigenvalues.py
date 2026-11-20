import numpy as np

A = np.array([[0., 1., 1., 0.],
              [1., 0., 1., 1.],
              [1., 1., 0., 1.],
              [0., 1., 1., 0.]])
values, vectors = np.linalg.eig(A)
idx = np.argmax(np.real(values))
dominant = np.real(values[idx])
v = np.abs(np.real(vectors[:, idx]))
scores = v / v.sum()
nodes = ["A", "B", "C", "D"]

print("BASE CASE")
print("Dominant eigenvalue:", dominant)
for node, score in zip(nodes, scores):
    print(f"{node}: {score:.4f}")
print("Verification error:", np.linalg.norm(A @ np.real(vectors[:, idx]) - dominant * np.real(vectors[:, idx])))

# Changed input: add a connection between nodes A and D
changed_A = A.copy()
changed_A[0, 3] = changed_A[3, 0] = 1
vals2, vecs2 = np.linalg.eig(changed_A)
i2 = np.argmax(np.real(vals2))
scores2 = np.abs(np.real(vecs2[:, i2]))
scores2 /= scores2.sum()
print("\nCHANGED CASE: connection added between A and D")
print(dict(zip(nodes, np.round(scores2, 4))))

# Related case: identify influential junctions in a road network
roads = np.array([[0., 1., 0.], [1., 0., 1.], [0., 1., 0.]])
rv, rvec = np.linalg.eig(roads)
ri = np.argmax(np.real(rv))
rs = np.abs(np.real(rvec[:, ri])); rs /= rs.sum()
print("\nRELATED CASE: road-junction importance", np.round(rs, 4))
