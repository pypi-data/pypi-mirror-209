import numpy as np
from typing import Union


def rela_to_abs(coords: list, resolution: list) -> np.array:
    '''
    相对坐标转换为绝对坐标。

    参数:
        coords (list): [center_x, center_y, width, height]

        resolution (list):  [width, height]
    
    返回:
        Union[np.array, list]: 绝对坐标
    '''
    coords = np.array(coords)
    if coords.dtype == float:
        w, h = resolution
        coords[:, ::2] *= w
        coords[:, 1::2] *= h
    return coords.astype(int).tolist()


def pnpoly(verts: list, testx: int, testy: int) -> bool:
    '''
    判断点是否在多边形内部, PNPoly算法。

    参数:
        verts (list): 由多边形顶点组成的列表, 例如[[129,89],[342,68],[397,206],[340,373],[87,268]]

        testx (int): 点的x坐标, 例如123

        testy (int): 点的y坐标, 例如234

    返回:
        True: 点在多边形内

        False: 点不在多边形内
    '''

    vertx = [xyvert[0] for xyvert in verts]
    verty = [xyvert[1] for xyvert in verts]
    nvert = len(verts)
    c = False
    j = nvert - 1
    for i in range(nvert):
        if ((verty[i] > testy) !=
            (verty[j] > testy)) and (testx < (vertx[j] - vertx[i]) *
                                     (testy - verty[i]) /
                                     (verty[j] - verty[i]) + vertx[i]):
            c = not c
        j = i
    return c


def persons_in_areas(persons_coords: list,
                     areas: list,
                     resolution: list = [],
                     h_offset: float = 0,
                     w_thresh: float = -1,
                     h_thresh: float = -1) -> bool:
    '''
    判断人是否在区域内, 支持单人坐标和多人坐标, 支持单区域和多区域, 支持过滤人检测框的宽度和高度, 支持人的位置偏移。
    坐标可以使用相对坐标或绝对坐标, 人和区域的坐标类型不一致时必须指定分辨率。使用过滤高度、宽度功能且人使用绝对坐标时须指定分辨率。

    参数:
        persons_coords (list): 单人[cx, cy, w, h], 多人[[cx1, cy1, w1, h1],[cx2, cy2, w2, h2],...]

        area (list): 单区域[[x1, y1], [x2, y2], [x3, y3]], 多区域[[[x1, y1], [x2, y2], [x3, y3]], [[x4, y4], [x5, y5], [x6, y6], [x7, 7]], ...]

        resolution (list): 视频分辨率, [width, height] 

        h_offset (float): 人的位置纵向偏移量, -0.5 <= h_thresh <= 0.5

        w_thresh (float): 检测框宽度过滤阈值, 0 <= w_thresh <= 1

        h_thresh (flost): 检测框高度过滤阈值, 0 <= h_thresh <= 1

    返回:
        True: 有人在区域内

        False: 无人在区域内
    '''

    # 全部转换为多人和多区域
    assert np.array(persons_coords).ndim in [1, 2]
    assert np.array(areas).ndim in [2, 3]
    if np.array(persons_coords).ndim == 1:
        persons_coords = [persons_coords]
    if np.array(areas).ndim == 2:
        areas = [areas]

    assert -0.5 <= h_offset <= 0.5

    # 判断是相对坐标还是绝对坐标(不严格)
    abs_person = True if np.array(persons_coords).dtype == int else False
    abs_area = True if np.array(areas[0]).dtype == int else False

    if abs_person != abs_area and not resolution:
        raise ValueError("未指定视频分辨率")

    # 如果坐标类型不一致就全部转为绝对坐标
    if abs_person == True and abs_area == False:
        for area in areas:
            area = rela_to_abs(area, resolution)
    elif abs_person == False and abs_area == True:
        persons_coords = rela_to_abs(persons_coords, resolution)

    # 宽度过滤
    if w_thresh != -1:
        assert 0 < w_thresh <= 1
        if abs_person:
            if not resolution:
                raise ValueError("未指定视频分辨率")
            else:
                w_thresh = int(w_thresh * resolution[0])
        persons_coords = [p for p in persons_coords if p[2] <= w_thresh]

    # 高度过滤
    if h_thresh != -1:
        assert 0 < h_thresh <= 1
        if abs_person:
            if not resolution:
                raise ValueError("未指定视频分辨率")
            else:
                h_thresh = int(h_thresh * resolution[1])
        persons_coords = [p for p in persons_coords if p[3] <= h_thresh]

    for p in persons_coords:
        cx = p[0]
        cy = p[1] + int(h_offset * p[3])
        for area in areas:
            if pnpoly(area, cx, cy):
                return True
    return False


def compute_polygon_area(x: list, y: list) -> float:
    '''
    计算多边形面积

    参数：
        x(list):[x1,x2,...,xn]
        y(list):[y1,y2,...,yn]

    返回：
        float :多边形面积

    '''

    point_num = len(x)
    if (point_num < 3): return 0.0

    s = y[0] * (x[point_num - 1] - x[1])
    for i in range(1, point_num):
        s += y[i] * (x[i - 1] - x[(i + 1) % point_num])
    return abs(s / 2.0)


def mean_fliter(x: list, y: list, step: int) -> tuple(list, list):
    '''
    自定义均值滤波：将数据滤波，然后按等间隔提取坐标值（中值滤波同时减少数据量，减少计算时间，提高效率）

    参数：
        x(list):[x1,x2,...,xn]

        y(list):[y1,y2,...,yn]

        step(int): n
    返回：
        #滤波和筛选后的坐标值

        x(list):[x1,x2,...,xn]

        y(list):[y1,y2,...,yn]
    '''
    result_x = np.array(x)
    result_y = np.array(y)

    column = step
    rank = int(np.size(result_x) / column)

    result_x = np.resize(result_x, (rank, column))
    result_y = np.resize(result_y, (rank, column))

    result_x = np.mean(result_x, axis=1)
    result_y = np.mean(result_y, axis=1)

    return result_x.tolist(), result_y.tolist()


def mid_filter(x: list, y: list, step: int) -> tuple(list, list):
    '''
    自定义中值滤波：将数据滤波，然后按等间隔提取坐标值（中值滤波同时减少数据量，减少计算时间，提高效率）

    参数：
        x(list):[x1,x2,...,xn]

        y(list):[y1,y2,...,yn]

        step(int): n
    返回：
        #滤波和筛选后的坐标值

        x(list):[x1,x2,...,xn]

        y(list):[y1,y2,...,yn]
    '''
    result_x = np.array(x)
    result_y = np.array(y)

    column = step
    rank = int(np.size(result_x) / column)

    result_x = np.resize(result_x, (rank, column))
    result_y = np.resize(result_y, (rank, column))

    result_x = np.median(result_x, axis=1)
    result_y = np.median(result_y, axis=1)

    return result_x.tolist(), result_y.tolist()


def get_scan_area(basis_x: list, basis_y: list, cur_x: list, cur_y: list,
                  step: int) -> float:
    '''
    计算当坐标和基础坐标构成多边形面积

    参数：
        basis_x(list):基础x坐标[x1,x2,x3,.....,xn]

        basis_y(list):基础y坐标[y1,y2,y3,.....,yn]

        cur_x(list): 当前x坐标[x1,x2,x3,.....,xn]

        cur_y(list): 当前y坐标[y1,y2,y3,.....,yn]
    返回：
        result(float):两次激光点云构成多边形的面积
    '''
    basis_x, basis_y = mean_fliter(basis_x, basis_y, step=step)
    basis_x = list(reversed(basis_x))
    basis_y = list(reversed(basis_y))

    cur_x, cur_y = mean_fliter(cur_x, cur_y, step)
    cur_x += basis_x
    cur_y += basis_y
    return compute_polygon_area(cur_x, cur_y)


def get_IOU(gt_box: Union(list, tuple), b_box: Union(list, tuple)) -> float:
    '''
        计算两个矩形区域的IOU

        参数：
            gt_box (list) : 真实区域坐标 [100,100,500,500] ,shape: [1,4]

            b_box (list) : 目标区域坐标 [150,150,400,400] ,shape: [1,4]

        返回：
            两个框的重叠程度(IOU)
    '''
    assert len(gt_box) == 4 and len(b_box) == 4, '请输入正确的坐标'
    gt_box = [int(i) for i in gt_box]
    b_box = [int(i) for i in b_box]

    width0 = gt_box[2] - gt_box[0]
    height0 = gt_box[3] - gt_box[1]
    width1 = b_box[2] - b_box[0]
    height1 = b_box[3] - b_box[1]
    max_x = max(gt_box[2], b_box[2])
    min_x = min(gt_box[0], b_box[0])
    width = width0 + width1 - (max_x - min_x)
    max_y = max(gt_box[3], b_box[3])
    min_y = min(gt_box[1], b_box[1])
    height = height0 + height1 - (max_y - min_y)

    interArea = width * height
    boxAArea = width0 * height0
    boxBArea = width1 * height1
    iou = interArea / (boxAArea + boxBArea - interArea)

    return iou


def compute_density(target_area: Union(list, tuple),
                    coords: Union(list, tuple)) -> tuple(int, float):
    '''
        输入一个目标区域，一组目标坐标，计算目标数量、密度

        参数：
            target_area (list) : [[129,89],[342,68],[397,206],[340,373],[87,268]] ,shape : [n,2]

            coords (list) : [[[左上x，左上y],[右下x,右下y]]]   [[[0,0],[500,500]],[[700,700],[400,400]], [[0,0],[100,100]],[[200,200],[300,300]]] ,shape : [3,n,2]

        返回：
            return (int、float) : 目标在区域中的数量、密度
    '''
    assert len(coords) != 0, '目标数量不能为0'
    assert np.array(target_area).shape[0] > 2, '区域坐标不能少于2'
    assert len(np.array(coords).shape) >= 3, '请输入正确目标坐标'
    assert np.array(coords).shape[1] >= 2 and np.array(
        coords).shape[2] == 2, '请输入正确区域坐标'
    number = len(coords)
    if type(coords) == list:
        coords = np.array(coords)
    minx = np.min(coords[:, :, 0])
    miny = np.min(coords[:, :, 1])
    maxx = np.max(coords[:, :, 0])
    maxy = np.max(coords[:, :, 1])
    p1, p2 = ((minx, miny, maxx, maxy)), (target_area[0][0], target_area[0][1],
                                          target_area[2][0], target_area[2][1])
    iou = get_IOU(p1, p2)
    # print(iou)
    density = iou / number
    return number, float(density)


if __name__ == '__main__':
    # persons_coords = [[0.1, 0.2, 0.2, 0.4]]
    # areas = [[0, 0], [0.1920, 0], [1920, 1080], [0, 1080]]
    # resolution = [1920, 1080]
    # print(
    #     persons_in_areas(persons_coords=persons_coords,
    #                      areas=areas,
    #                      w_thresh=0.3))
    target_area = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])
    coords = np.array([[[50, 50], [100, 100]], [[0, 0], [80, 80]],
                       [[0, 0], [5, 5]]])
    number, density = compute_density(target_area, coords)
    print(number, density, number * density)
    iou = get_IOU(np.array([50, 50, 100, 100]), np.array([0, 0, 100, 100]))
    print(iou)

    basis_x = [i for i in range(5)]
    basis_y = [0 for i in range(5)]
    cur_x = [i for i in range(5)]
    cur_y = [i for i in range(5)]
    res = get_scan_area(basis_x, basis_y, cur_x, cur_y, 2)
    print(res)