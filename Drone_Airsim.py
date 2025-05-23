import cosysairsim as airsim
import numpy as np

# your four UE-world corners (X, Y, Z) – we’ll ignore Z here
raw_corners = np.array([
    [ 76.9297, -77.8449, 8.790],
    [ 77.9950,  76.6607, 8.790],
    [-76.9277,  76.4324, 8.790],
    [-74.0643, -77.4082, 8.790]
])

# flight parameters
STRIP_SPACING = 50.0   # meters between each pass
FLIGHT_SPEED  = 10.0   # m/s

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# take off and hold altitude
client.takeoffAsync().join()
current_z = client.getMultirotorState().kinematics_estimated.position.z_val

# sort corners CCW
corners_xy = raw_corners[:, :2]
centroid   = corners_xy.mean(axis=0)
angles     = np.arctan2(corners_xy[:,1] - centroid[1],
                        corners_xy[:,0] - centroid[0])
corners_xy = corners_xy[np.argsort(angles)]

# find the two corners P→Q forming the longest edge
lengths = [np.linalg.norm(corners_xy[(i+1)%4] - corners_xy[i]) for i in range(4)]
i_long  = int(np.argmax(lengths))
P = corners_xy[i_long]
Q = corners_xy[(i_long+1)%4]

# unit “along-track” and unit “cross-track”
dir_along = (Q - P) / np.linalg.norm(Q - P)
dir_perp  = np.array([-dir_along[1], dir_along[0]])  # 90° rotate

# how many strips fit in the cross-track width
R = corners_xy[(i_long-1)%4]
width    = abs(np.dot(R - P, dir_perp))
n_strips = int(np.ceil(width / STRIP_SPACING))

for strip in range(n_strips):
    # compute this strip’s endpoints
    offset = dir_perp * strip * STRIP_SPACING
    A = P + offset
    B = Q + offset

    # alternate direction each strip
    if strip % 2 == 0:
        start, end = A, B
    else:
        start, end = B, A

    # 1) fly along-track
    client.moveToPositionAsync(float(start[0]), float(start[1]), current_z, FLIGHT_SPEED).join()
    client.hoverAsync().join()
    client.moveToPositionAsync(float(end[0]),   float(end[1]),   current_z, FLIGHT_SPEED).join()
    client.hoverAsync().join()

    # 2) if not last strip, move purely cross-track
    if strip < n_strips - 1:
        cross_pt = end + dir_perp * STRIP_SPACING
        client.moveToPositionAsync(float(cross_pt[0]), float(cross_pt[1]), current_z, FLIGHT_SPEED).join()
        client.hoverAsync().join()

# return & land
client.moveToPositionAsync(0, 0, current_z, FLIGHT_SPEED).join()
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)