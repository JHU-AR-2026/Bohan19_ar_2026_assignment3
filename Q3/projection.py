def project(point, width, height, near, far, fx, fy, ox, oy):
    matrix = [
        [2 * fx / width, 0, 1 - 2 * ox / width, 0],
        [0, 2 * fy / height, 1 - 2 * oy / height, 0],
        [0, 0, -(far + near) / (far - near),
         -2 * far * near / (far - near)],
        [0, 0, -1, 0],
    ]

    homogeneous_point = (*point, 1)
    clip = []
    for row in matrix:
        clip.append(sum(row[i] * homogeneous_point[i] for i in range(4)))
    w = clip[3]
    ndc = tuple(value / w for value in clip[:3])
    pixels = ((ndc[0] + 1) * width / 2, (ndc[1] + 1) * height / 2)
    return matrix, clip, ndc, pixels


if __name__ == "__main__":
    point = (0.3, -0.15, -6.0)
    width, height = 800, 600
    near, far = 0.2, 20
    fx, fy = 800, 800
    ox, oy = 400, 400

    matrix, clip, ndc, pixels = project(
        point, width, height, near, far, fx, fy, ox, oy
    )

    print("Projection matrix:")
    for row in matrix:
        print(row)
    print("Clip:", clip)
    print("NDC:", ndc)
    print("Pixels:", pixels)
