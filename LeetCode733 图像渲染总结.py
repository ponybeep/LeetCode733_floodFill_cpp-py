# 公司 步微科技
# 编写人    ponybeep
# 开发时间：2022-5-9 9:50
# 题目描述：
# 有一幅以m x n 的二维整数数组表示的图画image,其中image[i][j]表示该图画的像素值大小
# 你也被给予三个整数sr, sc 和newColor。你应该从像素image[sr][sc]开始对图像进行上色填充
# 为了完成上色工作，从初始像素开始，记录初始坐标的上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他
# 们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。
# 最后返回 经过上色渲染后的图像 。
# 示例：
# 输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
# 方法一：深度优先（使用栈）
import collections
class Solution1:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        if image[sr][sc] == newColor:
            return image
        stack, currColor = [(sr,sc)], image[sr][sc]
        while stack:
            point = stack.pop()
            image[point[0]][point[1]] = newColor
            for dx, dy in [(point[0], point[1] - 1), (point[0], point[1] + 1), (point[0] - 1, point[1]), (point[0] + 1, point[1])]:
                if 0 <= dx < len(image) and 0 <= dy < len(image[0]) and image[dx][dy] == currColor:
                    stack.append((dx,dy))
        return image


# 定义实参
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
newColor = 2
# 调用方法一的类
print('--------------------方法一 深度优先（使用栈）---------------------')
solution = Solution1()
newImage = solution.floodFill(image, sr, sc, newColor)
print(newImage)         # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


# 方法二 深度优先（使用递归）
class Solution2:
    def floodFill(self,image:list[list[int]],sr:int,sc:int,newColor:int) -> list[list[int]]:
        if newColor != image[sr][sc]:
            curColor, image[sr][sc] = image[sr][sc], newColor
            for dx, dy in [(sr,sc+1),(sr,sc-1),(sr+1,sc),(sr-1,sc)]:
                if 0<=dx<len(image) and 0<=dy<len(image[0]) and image[dx][dy]==curColor:
                    self.floodFill(image,dx,dy,newColor)
        return image


# 调用方法二的类
print('---------------------方法二 深度优先（使用递归）-----------------------')
solution = Solution2()
newImage = solution.floodFill(image, sr, sc, newColor)
print(newImage)         # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

# 方法三 深度优先（使用递归，代码长一点，嵌套方法）
class Solution3:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image


# 调用方法三的类
print('------------------方法三 深度优先（使用递归，代码长一点，嵌套方法）--------------------------')
solution = Solution3()
newImage = solution.floodFill(image, sr, sc, newColor)
print(newImage)         # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


# 方法四 广度优先算法（使用队列）
class Solution4:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        currColor = image[sr][sc]
        if currColor == newColor:
            return image
        m, n = len(image), len(image[0])
        que = collections.deque([(sr, sc)])
        image[sr][sc] = newColor
        while que:
            x, y = que.popleft()
            for mx, my in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if 0 <= mx < m and 0 <= my < n and image[mx][my] == currColor:
                    que.append((mx, my))
                    image[mx][my] = newColor
        return image


# 调用方法四的类
print('--------------------方法四 广度优先算法（使用队列）------------------------')
solution = Solution4()
newImage = solution.floodFill(image, sr, sc, newColor)
print(newImage)         # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

# 总结：使用堆栈或者队列的时候，一般采用while->for->if 的格式。
# while判断队列或者堆栈是否为空，不为空则删除最后一个元素
# for 遍历所有与当前元素挨着的元素（上下左右）
# if 判断挨着的元素是否满足条件，满足条件则补充队列或者堆栈
# 若在while后面进行上色的操作，则if后面不需要进行上色
# 若在if后面进行上色的操作，则while后面不需要进行上色，但要在while循环前面即对第一个元素进行上色image[sr][sc] = newColor




