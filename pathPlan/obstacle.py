from pyglet import gl
import math
import shared


def create_indexed_vertices(x, y, radius, sides=24):
    vertices = [x, y]
    for side in range(sides):
        angle = side * 2.0 * math.pi / sides
        vertices.append(x + math.cos(angle) * radius)
        vertices.append(y + math.sin(angle) * radius)
    # Add a degenerated vertex
    vertices.append(x + math.cos(0) * radius)
    vertices.append(y + math.sin(0) * radius)

    indices = []
    for side in range(1, sides+1):
        indices.append(0)
        indices.append(side)
        indices.append(side + 1)
    return vertices, indices   

def create_circle(x, y, radius, batch):
    circle, indices = create_indexed_vertices(x, y, radius)
    vertex_count = len(circle) // 2
    return (vertex_count, gl.GL_TRIANGLES, None,
                indices,
                ('v2f', circle), 
                ('c4f', (1, 1, 1, 0.8) * vertex_count)) 

'''
class Obstacle(object):
    def __init__(self, x, y, width, height):
        # right now we restrict obstacles to rectangles, eventually extend to polygons using triangle fans
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = None

    def add_to_default_batch(self):
        """
        Adds the obstacle as a GL_QUAD, does not allow obstacles less than step size
        :return:
        """
        if self.y < 50:
            self.height += self.y - 50
            self.y = 50
        if self.width < shared.STEP_SIZE or self.height < shared.STEP_SIZE:
            self.delete()
            return
        self.shape = shared.batch.add(4, gl.GL_QUADS, None,
                                      ('v2f', (self.x, self.y,
                                               self.x + self.width, self.y,
                                               self.x + self.width, self.y + self.height,
                                               self.x, self.y + self.height)))

    def collides_with(self, x, y):
        """
        :param x: x position of other point
        :param y: y position of other point
        :return: Boolean True if a collision occurs
        """
        return self.x + self.width > x > self.x and self.y + self.height > y > self.y

    def delete(self):
        """
        Deletes the obstacle
        Deletes the graphics object if it exists then remove from the obstacles list
        :return: None
        """
        if self.shape is not None:
            self.shape.delete()
        if self in shared.obstacles:
            shared.obstacles.remove(self)

'''

class Obstacle(object):
    def __init__(self, x, y, radius):
        # right now we restrict obstacles to rectangles, eventually extend to polygons using triangle fans
        self.x = x
        self.y = y
        self.radius = radius
        self.shape = None
        self.groupID = 1



    def add_to_default_batch(self):
        """
        Adds the obstacle as a GL_QUAD, does not allow obstacles less than step size
        :return:
        """

        '''
        self.shape = shared.batch.add(4, gl.GL_QUADS, None,
                                      ('v2f', (self.x, self.y,
                                               self.x + self.width, self.y,
                                               self.x + self.width, self.y + self.height,
                                               self.x, self.y + self.height)))
        
        numPoints = 50
        verts = []
        for i in range(numPoints):
            angle = math.radians(float(i)/numPoints * 360.0)
            x = self.radius*cos(angle) + self.x
            y = self.radius*sin(angle) + self.y
            verts += [int(x),int(y)]
        
        '''
        data = create_circle(self.x, self.y, self.radius, shared.batch)

        self.shape = shared.batch.add_indexed(data[0], data[1], data[2], data[3], data[4], data[5])

        #self.shape = shared.batch.add(numPoints, gl.GL_POLYGON, None,
        #                             ('v2f', verts))

        

    


    def collides_with(self, x, y):
        """
        :param x: x position of other point
        :param y: y position of other point
        :return: Boolean True if a collision occurs
        """
        return ((self.x - x)**2 + (self.y - y)**2)**.5 < self.radius 

    def delete(self):
        """
        Deletes the obstacle
        Deletes the graphics object if it exists then remove from the obstacles list
        :return: None
        """
        if self.shape is not None:
            self.shape.delete()
        if self in shared.obstacles:
            shared.obstacles.remove(self)