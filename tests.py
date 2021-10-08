import pygame3D

def testIntersectionHelper(front, back, cam):
    # ensure that intersection calculating is idempotent
    x = pygame3D.find_intersection(front, back, cam)
    return x.equals(pygame3D.find_intersection(x, back, cam)) and x.equals(pygame3D.find_intersection(front, x, cam))

def testIntersection():
    camera = pygame3D.Camera()
    count = 0
    for i in range(0, 100, 10):
        for j in range(0, 100, 10):
            # make a point and push it away from the camera in one direction
            front = pygame3D.Vec3([0,i,j]).add(camera.n.scale(100))
            # make another point and push it away from the camera in another direction
            back = pygame3D.Vec3([j,0,i]).add(camera.n.scale(-100))
            # test the two points
            if not testIntersectionHelper(front, back, camera):
                print(f"Failed on test number {count}. The points were {front} and {back}.")
            print(f"{front}, {pygame3D.find_intersection(front, back, camera)}, {back}")
            count += 1
    print(f"Passed all of {count} tests.")

if __name__ == "__main__":
    testIntersection()
