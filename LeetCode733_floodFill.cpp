#define _CRT_SECURE_NO_WARNINGS 1
using namespace std;
#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <queue>
#include <stack>
//题目描述
//有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
//
//你也被给予三个整数 sr, sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。
//
//为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。
//
//最后返回 经过上色渲染后的图像 。

//实例：
//输入：image = [[1,1,1],[1,1,0],[1,0,1]]
//输出: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
//解析 : 在图像的正中间，(坐标(sr, sc) = (1, 1)), 在路径上所有符合条件的像素点的颜色都被更改成2。
//注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。


// 方法一 广度优先（使用队列实现）
class Solution1{
public:
	const int dx[4] = { 0,0,1,-1 };
	const int dy[4] = { 1,-1,0,0 };
	vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor)
	{
		int curColor = image[sr][sc];
		if (curColor == newColor)
		{
			return image;
		}
		int m = image.size(), n = image[0].size();
		image[sr][sc] = newColor;
		queue <pair<int, int>> que;
		que.emplace(sr, sc);
		while (!que.empty())
		{
			int x = que.front().first, y = que.front().second;
			que.pop();
			for (int i = 0; i < 4; i++)
			{
				int mx = x + dx[i], my = y + dy[i];
				if (mx >= 0 && mx < m && my >= 0 && my < n && image[mx][my] == curColor)
				{
					que.emplace(mx, my);
					image[mx][my] = newColor;
				}
			}
		}
		return image;

	}
};


//方法一的测试
void test01()
{

	vector<int> imager1 = { 1,1,1,1 };
	vector<int> imager2 = { 1,1,0,1 };
	vector<int> imager3 = { 1,0,0,1 };
	vector<vector<int>> image = { imager1,imager2,imager3 };
	int m = image.size(), n = image[0].size();
	cout << "原图像为：" << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << image[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	int sr = 1, sc = 1, newColor = 3;
	Solution1 solution1;
	vector<vector<int>> ans = solution1.floodFill(image, sr, sc, newColor);
	cout << "使用方法一 广度优先（队列实现）后的图像为：" << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << ans[i][j] << " ";
		}
		cout << endl;
	}
	printf("---------------------------------\n");


}


//方法二 深度优先（使用堆栈实现）
class Solution2 {
public:
	const int dx[4] = { 0,0,1,-1 };
	const int dy[4] = { 1,-1,0,0 };
	vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor)
	{
		if (image[sr][sc] == newColor)
		{
			return image;
		}
		int m = image.size(), n = image[0].size();
		int curColor = image[sr][sc];
		stack<pair<int, int>> stack;
		stack.emplace(sr, sc);
		while (!stack.empty())
		{
			int x = stack.top().first, y = stack.top().second;
			stack.pop();
			image[x][y] = newColor;
			for (int i = 0; i < 4; i++)
			{
				int mx = x + dx[i], my = y + dy[i];
				if (mx >= 0 && mx < m && my >= 0 && my < n && image[mx][my] == curColor)
				{
					stack.emplace(mx, my);
				}
			}
		}
		return image;
	}
};


//方法二的测试
void test02()
{

	vector<int> imager1 = { 1,1,1,1 };
	vector<int> imager2 = { 1,1,0,1 };
	vector<int> imager3 = { 1,0,0,1 };
	vector<vector<int>> image = { imager1,imager2,imager3 };
	int m = image.size(), n = image[0].size();
	cout << "原图像为：" << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << image[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	int sr = 1, sc = 1, newColor = 3;
	Solution2 solution2;
	vector<vector<int>> ans = solution2.floodFill(image, sr, sc, newColor);
	cout << "使用方法二 深度度优先（堆栈实现）后的图像为：" << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << ans[i][j] << " ";
		}
		cout << endl;
	}
	printf("---------------------------------\n");


}


int main() {
	test01();
	test02();


	system("pause");
	return 0;
}