import numpy as np

points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
angle = np.deg2rad(45)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
scale = np.array([[2., 0.], [0., 1.5]])
transformation = rotation @ scale
transformed = points @ transformation.T

print("BASE CASE: rotate 45 degrees and scale x by 2, y by 1.5")
print("Original points:\n", points)
print("Transformed points:\n", np.round(transformed, 3))
print("Determinant:", np.linalg.det(transformation))

# Changed parameter: use a 90-degree rotation
angle2 = np.deg2rad(90)
rotation2 = np.array([[np.cos(angle2), -np.sin(angle2)],
                      [np.sin(angle2),  np.cos(angle2)]])
changed = points @ (rotation2 @ scale).T
print("\nCHANGED CASE: rotation changed to 90 degrees")
print(np.round(changed, 3))

# Related case: transform four map coordinates by translation and scaling
map_points = np.array([[1., 2.], [3., 4.], [5., 2.]])
map_scaled = map_points * 1000 + np.array([500000, 9900000])
print("\nRELATED CASE: local map coordinates converted to scaled grid coordinates")
print(map_scaled)
