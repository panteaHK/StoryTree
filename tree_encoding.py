import numpy as np

class TreeEncoding:
    ipe_pre = """<?xml version="1.0"?>
                <!DOCTYPE ipe SYSTEM "ipe.dtd">
                <ipe version="70218" creator="Ipe 7.2.21">
                <preamble>\\renewcommand{\\familydefault}{\sfdefault}</preamble>
                <ipestyle name="extendedcolors">
                <color name="CB light blue" value="0.651 0.807 0.89"/>
                <color name="CB dark blue" value="0.121 0.47 0.705"/>
                <color name="CB light green" value="0.698 0.874 0.541"/>
                <color name="CB dark green" value="0.2 0.627 0.172"/>
                <color name="CB light red" value="0.984 0.603 0.6"/>
                <color name="CB dark red" value="0.89 0.102 0.109"/>
                <color name="CB light orange" value="0.992 0.749 0.435"/>
                <color name="CB dark orange" value="1 0.498 0"/>
                <color name="CB light purple" value="0.792 0.698 0.839"/>
                <color name="CB dark purple" value="0.415 0.239 0.603"/>
                <color name="CB yellow" value="1 1 0.6"/>
                <color name="CB brown" value="0.694 0.349 0.157"/>
                <color name="CART 1" value="0.145 0.737 0.612"/>
                <color name="CART 2" value="0.533 0.78 0.396"/>
                <color name="CART 3" value="0.561 0.737 0.757"/>
                <color name="CART 4" value="0.604 0.839 0.741"/>
                <color name="CART 5" value="0.706 0.592 0.506"/>
                <color name="CART 6" value="0.733 0.718 0.349"/>
                <color name="CART 7" value="0.831 0.878 0.353"/>
                <color name="CART 8" value="0.835 0.725 0.541"/>
                <color name="CART 9" value="0.867 0.529 0.475"/>
                <color name="CART 10" value="0.996 0.965 0.608"/>
                <color name="CART 11" value="0.996 0.859 0.706"/>
                <color name="CART 12" value="0.98 0.714 0.58"/>
                <color name="CART 13" value="1 0.8 0.302"/>
                <color name="Gray 0.0" value="0"/>
                <color name="Gray 0.1" value="0.1"/>
                <color name="Gray 0.2" value="0.2"/>
                <color name="Gray 0.3" value="0.3"/>
                <color name="Gray 0.4" value="0.4"/>
                <color name="Gray 0.5" value="0.5"/>
                <color name="Gray 0.6" value="0.6"/>
                <color name="Gray 0.7" value="0.7"/>
                <color name="Gray 0.8" value="0.8"/>
                <color name="Gray 0.9" value="0.9"/>
                <color name="Gray 1.0" value="1"/>
                <dashstyle name="W dashed normal" value="[1 1.7] 0"/>
                <dashstyle name="W dashed heavier" value="[2 3] 0"/>
                <dashstyle name="W dashed fat" value="[3 5.1] 0"/>
                <dashstyle name="W dashed ultrafat" value="[5 8.5] 0"/>
                <dashstyle name="W dot normal" value="[0.01 0.8] 0"/>
                <dashstyle name="W dot heavier" value="[0.01 1.6] 0"/>
                <dashstyle name="W dot fat" value="[0.01 2.4] 0"/>
                <dashstyle name="W dot ultrafat" value="[0.01 4] 0"/>
                </ipestyle>
                <ipestyle name="pptcolors">
                <color name="PPT blue" value="0 0.459 0.965"/>
                <color name="PPT green" value="0 0.69 0.314"/>
                <color name="PPT gray" value="0.647"/>
                <color name="PPT red" value="0.753 0 0"/>
                <color name="PPT purple" value="0.439 0.188 0.627"/>
                <color name="PPT yellow" value="1 0.753 0"/>
                </ipestyle>
                <ipestyle name="arrows">
                <symbol name="arrow/circle(spx)" transformations="translations">
                <path stroke="sym-stroke" pen="sym-pen">
                0.5 0 0 0.5 0 0 e
                </path>
                </symbol>
                <symbol name="arrow/disk(spx)" transformations="translations">
                <group>
                <path fill="sym-stroke">
                0.5 0 0 0.5 0 0 e
                </path>
                <path stroke="sym-stroke" pen="sym-pen">
                0.5 0 0 0.5 0 0 e
                </path>
                </group>
                </symbol>
                <symbol name="arrow/fdisk(spx)" transformations="translations">
                <group>
                <path fill="white">
                0.5 0 0 0.5 0 0 e
                </path>
                <path stroke="sym-stroke" pen="sym-pen">
                0.5 0 0 0.5 0 0 e
                </path>
                </group>
                </symbol>
                <symbol name="arrow/box(spx)" transformations="translations">
                <path stroke="sym-stroke" pen="sym-pen">
                -0.5 -0.5 m
                0.5 -0.5 l
                0.5 0.5 l
                -0.5 0.5 l
                h
                </path>
                </symbol>
                <symbol name="arrow/square(spx)" transformations="translations">
                <path fill="sym-stroke">
                -0.5 -0.5 m
                0.5 -0.5 l
                0.5 0.5 l
                -0.5 0.5 l
                h
                </path>
                </symbol>
                <symbol name="arrow/fsquare(spx)" transformations="translations">
                <group>
                <path fill="white">
                -0.5 -0.5 m
                0.5 -0.5 l
                0.5 0.5 l
                -0.5 0.5 l
                h
                </path>
                <path stroke="sym-stroke" pen="sym-pen">
                -0.5 -0.5 m
                0.5 -0.5 l
                0.5 0.5 l
                -0.5 0.5 l
                h
                </path>
                </group>
                </symbol>
                <symbol name="arrow/cross(spx)" transformations="translations">
                <group>
                <path stroke="sym-stroke" pen="sym-pen">
                -0.5 -0.5 m
                0.5 0.5 l
                h
                </path>
                <path stroke="sym-stroke" pen="sym-pen">
                -0.5 0.5 m
                0.5 -0.5 l
                h
                </path>
                </group>
                </symbol>
                <symbol name="arrow/whiskers(spx)" transformations="translations">
                <path stroke="sym-stroke" pen="sym-pen">
                0 -0.5 m
                0 0.5 l
                h
                </path>
                </symbol>
                </ipestyle>
                <ipestyle name="grids">
                <gridsize name="1 pt" value="1"/>
                <gridsize name="2 pts" value="2"/>
                <gridsize name="4 pts" value="4"/>
                <gridsize name="8 pts (~3 mm)" value="8"/>
                <gridsize name="16 pts (~6 mm)" value="16"/>
                <gridsize name="32 pts (~12 mm)" value="32"/>
                <gridsize name="10 pts (~3.5 mm)" value="10"/>
                <gridsize name="20 pts (~7 mm)" value="20"/>
                <gridsize name="14 pts (~5 mm)" value="14"/>
                <gridsize name="28 pts (~10 mm)" value="28"/>
                <gridsize name="56 pts (~20 mm)" value="56"/>
                <anglesize name="90 deg" value="90"/>
                <anglesize name="60 deg" value="60"/>
                <anglesize name="45 deg" value="45"/>
                <anglesize name="30 deg" value="30"/>
                <anglesize name="22.5 deg" value="22.5"/>
                <anglesize name="10 deg" value="10"/>
                <anglesize name="5 deg" value="5"/>
                </ipestyle>
                <ipestyle name="sizes">
                <pen name="heavier" value="0.8"/>
                <pen name="fat" value="1.2"/>
                <pen name="ultrafat" value="2"/>
                <pen name="1" value="1"/>
                <pen name="2" value="2"/>
                <pen name="3" value="3"/>
                <pen name="4" value="4"/>
                <pen name="5" value="5"/>
                <pen name="6" value="6"/>
                <pen name="7" value="7"/>
                <pen name="8" value="8"/>
                <pen name="9" value="9"/>
                <pen name="10" value="10"/>
                <symbolsize name="large" value="5"/>
                <symbolsize name="1" value="1"/>
                <symbolsize name="2" value="2"/>
                <symbolsize name="3" value="3"/>
                <symbolsize name="4" value="4"/>
                <symbolsize name="5" value="5"/>
                <symbolsize name="6" value="6"/>
                <symbolsize name="7" value="7"/>
                <symbolsize name="8" value="8"/>
                <symbolsize name="9" value="9"/>
                <symbolsize name="10" value="10"/>
                <symbolsize name="small" value="2"/>
                <symbolsize name="tiny" value="1.1"/>
                <arrowsize name="large" value="10"/>
                <arrowsize name="small" value="5"/>
                <arrowsize name="tiny" value="3"/>
                </ipestyle>
                <ipestyle name="text">
                <textsize name="large" value="\large"/>
                <textsize name="small" value="\small"/>
                <textsize name="tiny" value="\\tiny"/>
                <textsize name="Large" value="\Large"/>
                <textsize name="LARGE" value="\LARGE"/>
                <textsize name="huge" value="\huge"/>
                <textsize name="Huge" value="\Huge"/>
                <textsize name="footnote" value="\\footnotesize"/>
                <textstyle name="center" begin="\\begin{center}" end="\end{center}"/>
                <textstyle name="itemize" begin="\\begin{itemize}" end="\end{itemize}"/>
                <textstyle name="item" begin="\\begin{itemize}\item{}" end="\end{itemize}"/>
                </ipestyle>
                <ipestyle name="transparency">
                <opacity name="10%" value="0.1"/>
                <opacity name="20%" value="0.2"/>
                <opacity name="30%" value="0.3"/>
                <opacity name="40%" value="0.4"/>
                <opacity name="50%" value="0.5"/>
                <opacity name="60%" value="0.6"/>
                <opacity name="70%" value="0.7"/>
                <opacity name="80%" value="0.8"/>
                <opacity name="90%" value="0.9"/>
                </ipestyle>
                <ipestyle name="trimmed">
                <symbol name="arrow/arc(spx)">
                <path stroke="sym-stroke" fill="sym-stroke" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/farc(spx)">
                <path stroke="sym-stroke" fill="white" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/ptarc(spx)">
                <path stroke="sym-stroke" fill="sym-stroke" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -0.8 0 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/fptarc(spx)">
                <path stroke="sym-stroke" fill="white" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -0.8 0 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="mark/circle(sx)" transformations="translations">
                <path fill="sym-stroke">
                0.6 0 0 0.6 0 0 e
                0.4 0 0 0.4 0 0 e
                </path>
                </symbol>
                <symbol name="mark/disk(sx)" transformations="translations">
                <path fill="sym-stroke">
                0.6 0 0 0.6 0 0 e
                </path>
                </symbol>
                <symbol name="mark/fdisk(sfx)" transformations="translations">
                <group>
                <path fill="sym-fill">
                0.5 0 0 0.5 0 0 e
                </path>
                <path fill="sym-stroke" fillrule="eofill">
                0.6 0 0 0.6 0 0 e
                0.4 0 0 0.4 0 0 e
                </path>
                </group>
                </symbol>
                <symbol name="mark/box(sx)" transformations="translations">
                <path fill="sym-stroke" fillrule="eofill">
                -0.6 -0.6 m
                0.6 -0.6 l
                0.6 0.6 l
                -0.6 0.6 l
                h
                -0.4 -0.4 m
                0.4 -0.4 l
                0.4 0.4 l
                -0.4 0.4 l
                h
                </path>
                </symbol>
                <symbol name="mark/square(sx)" transformations="translations">
                <path fill="sym-stroke">
                -0.6 -0.6 m
                0.6 -0.6 l
                0.6 0.6 l
                -0.6 0.6 l
                h
                </path>
                </symbol>
                <symbol name="mark/fsquare(sfx)" transformations="translations">
                <group>
                <path fill="sym-fill">
                -0.5 -0.5 m
                0.5 -0.5 l
                0.5 0.5 l
                -0.5 0.5 l
                h
                </path>
                <path fill="sym-stroke" fillrule="eofill">
                -0.6 -0.6 m
                0.6 -0.6 l
                0.6 0.6 l
                -0.6 0.6 l
                h
                -0.4 -0.4 m
                0.4 -0.4 l
                0.4 0.4 l
                -0.4 0.4 l
                h
                </path>
                </group>
                </symbol>
                <symbol name="mark/cross(sx)" transformations="translations">
                <group>
                <path fill="sym-stroke">
                -0.43 -0.57 m
                0.57 0.43 l
                0.43 0.57 l
                -0.57 -0.43 l
                h
                </path>
                <path fill="sym-stroke">
                -0.43 0.57 m
                0.57 -0.43 l
                0.43 -0.57 l
                -0.57 0.43 l
                h
                </path>
                </group>
                </symbol>
                <symbol name="arrow/fnormal(spx)">
                <path stroke="sym-stroke" fill="white" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/pointed(spx)">
                <path stroke="sym-stroke" fill="sym-stroke" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -0.8 0 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/fpointed(spx)">
                <path stroke="sym-stroke" fill="white" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -0.8 0 l
                -1 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/linear(spx)">
                <path stroke="sym-stroke" pen="sym-pen">
                -1 0.333 m
                0 0 l
                -1 -0.333 l
                </path>
                </symbol>
                <symbol name="arrow/fdouble(spx)">
                <path stroke="sym-stroke" fill="white" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -1 -0.333 l
                h
                -1 0 m
                -2 0.333 l
                -2 -0.333 l
                h
                </path>
                </symbol>
                <symbol name="arrow/double(spx)">
                <path stroke="sym-stroke" fill="sym-stroke" pen="sym-pen">
                0 0 m
                -1 0.333 l
                -1 -0.333 l
                h
                -1 0 m
                -2 0.333 l
                -2 -0.333 l
                h
                </path>
                </symbol>
                <tiling name="falling" angle="-60" step="4" width="1"/>
                <tiling name="rising" angle="30" step="4" width="1"/>
                </ipestyle>
                """
    layout = """<ipestyle name="canvas_size">
                <layout paper="{} {}" origin="0 0" frame="{} {}"/>
                </ipestyle>
                <page>
                <layer name="alpha"/>
                <view layers="alpha" active="alpha"/>
                """

    ipe_post = """
                </page>
                </ipe>"""
    trimming_summary = []
    kcenter_summary = []
    trimmed = set()
    UNIT = 6
    RADIUS = 1 * UNIT
    leaf_scale = 1.7
    line_width = 1
    trimmed_square = 3
    salient_square = 3
    digits_round = 5
    horizontals = []
    verticals = []
    casing = 2
    y_scale = 2 
    x_scale = 2 
    x_min, y_min = 0, 0
    x_max, y_max = 500, 500

    def __init__(self, adjacency, births, n_leaves, n_nodes, trimming_summary, kcenter_summary, trimmed, important, SCALE = 1):
        self.x_scale *= SCALE
        self.y_scale *= SCALE
        self.adjacency = adjacency
        for k in self.adjacency.keys():
            self.adjacency[k] = np.sort(self.adjacency[k])
        self.n_leaves = n_leaves
        self.n_nodes = n_nodes
        self.births = births
        self.tree_nodes = {}
        self.tree_edges = {}
        self.node_position = {}
        self.edge_position = {}
        self.trimming_summary = trimming_summary
        self.kcenter_summary = kcenter_summary
        self.important_nodes = important
        self.process_trimmed_parts(trimmed)

    def process_trimmed_parts(self, trimmed):
        self.trimmed = set(trimmed)
        tobechecked = trimmed
        while len(tobechecked):
            node = tobechecked.pop()
            if node >= self.n_leaves:
                r, l = self.adjacency[node]
                self.trimmed.add(r)
                self.trimmed.add(l)
                tobechecked.append(r)
                tobechecked.append(l)

    def is_leaf(self, id):
        return id < self.n_leaves

    def node_color(self, id):
        stroke = "black"
        fill = "1"
        in_trimming = False
        in_kcenter = False
        if id in self.trimmed:
            stroke = "Gray 0.5"
        if id in self.trimming_summary:
            in_trimming = True
        if id in self.kcenter_summary:
            in_kcenter = True
        if in_kcenter and in_trimming:
            stroke = "CB dark purple"
            fill = "CB light purple"
        elif in_trimming:
            stroke = "CB dark red"
            fill = "CB light red"
        elif in_kcenter:
            stroke = "CB dark blue"
            fill = "CB light blue"
        return f"""stroke = "{stroke}" """, f"""fill = "{fill}" """

    def edge_color(self, n1, n2):
        stroke ="black"
        if n1 in self.trimmed or n2 in self.trimmed:
            stroke = "Gray 0.5"
        return f"""stroke = "{stroke}" """

    def get_x_coordinate(self, id):
        if self.is_leaf(id):
            return (id + 1) * self.x_scale * self.RADIUS
        r, l = self.adjacency[id]
        r_leaf = self.is_leaf(r)
        l_leaf = self.is_leaf(l)
        if r_leaf and l_leaf:
            return min(self.node_position[r][0], self.node_position[l][0])
        if not r_leaf and l_leaf:
            return self.node_position[r][0]
        if not l_leaf and r_leaf:
            return self.node_position[l][0]
        bottom_of_r = r
        bottom_of_l = l
        xr = self.node_position[r][0]
        xl = self.node_position[l][0]

        while True:
            n1, n2 = self.adjacency[bottom_of_r]
            if self.is_leaf(n1) and self.is_leaf(n2):
                break
            if self.node_position[n1][0] == xr:
                bottom_of_r = n1
            else:
                bottom_of_r = n2

        while True:
            n1, n2 = self.adjacency[bottom_of_l]
            if self.is_leaf(n1) and self.is_leaf(n2):
                break
            if self.node_position[n1][0] == xl:
                bottom_of_l = n1
            else:
                bottom_of_l = n2

        if bottom_of_r < bottom_of_l:
            return xr
        else:
            return xl

    def get_y_coordinate(self, id):
        return (id - self.n_leaves + 1)

    def node_visualization(self, id, x, y):
        if id in self.important_nodes:
            return f"""<use name="mark/fsquare(sfx)" pos="{x} {y}" size="{self.salient_square}" stroke="CB dark green" fill="CB light green"/>\n"""
        is_leaf = self.is_leaf(id)
        if not is_leaf and id in self.trimmed:
            return f"""<use name="mark/square(sx)" pos="{x} {y}" size="{self.trimmed_square}" stroke="Gray 0.5"/>\n"""
        if not is_leaf:
            return f"""<use name="mark/square(sx)" pos="{x} {y}" size="{self.trimmed_square}" stroke="black"/>\n"""

        stroke, fill = self.node_color(id)
        x_offset, y_offset = -2, -3
        if id > 9:
            x_offset = -5
        vis = f"""\n<path layer="alpha" {stroke} {fill} pen= "{self.line_width}" cap="1" join="1">\n {self.RADIUS * self.leaf_scale} 0 0 {self.RADIUS * self.leaf_scale} {x} {y} e\n</path>"""
        vis = f"""\n<path layer="alpha" {stroke} {fill} pen="{self.line_width}" cap="1" join="1">
            {x-self.RADIUS} {(y)-self.RADIUS} m
            {x-self.RADIUS} {(y)+self.RADIUS} l
            {x+self.RADIUS} {(y)+self.RADIUS} l
            {x+self.RADIUS} {(y)-self.RADIUS} l
            h
            </path>"""
        vis += f"""\n<text pos="{x + x_offset} {y + y_offset}" {stroke}type="label" valign="baseline" style="normal">\\footnotesize {id}</text>"""
        self.x_min = np.min([self.x_min, x-self.RADIUS])
        self.y_min = np.min([self.y_min, y-self.RADIUS])
        self.x_max = np.min([self.x_min, x+self.RADIUS])
        self.y_max = np.min([self.y_min, y+self.RADIUS])
        return vis

    def add_node(self, id, y):
        if id in self.node_position.keys():
            return
        x = self.get_x_coordinate(id)
        self.tree_nodes[id] = self.node_visualization(id, x, y)
        self.node_position[id] = (x, y)

    def add_edge(self, n1, n2):
        edge = (n1, n2)
        x1, y1 = self.node_position[n1]
        x2, y2 = self.node_position[n2]
        stroke = self.edge_color(n1, n2)
        if y1 == y2:
            vis = f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{x1} {y1} m\n{x2} {y2} l\n</path>\n"""
            self.tree_edges[edge] = vis
            self.horizontals.append(vis)
        elif x1 == x2:
            s = abs(y1 - y2)
            vis = f"""<path stroke="white" pen="{self.line_width+self.casing}" cap="1" join="1">\n{x1} {y1 + self.casing*((y2-y1)/s)} m\n{x2} {y2 + self.casing*((y1-y2)/s)} l\n</path>\n"""
            vis += f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{x1} {y1} m\n{x2} {y2} l\n</path>\n"""
            self.tree_edges[edge] = vis
            self.verticals.append(vis)
        else:
            if n1 < n2:
                mx = x1
                my = y2
            else:
                mx = x2
                my = y1

            if mx == x1:
                s = abs(y1 - my)
                vis = f"""<path stroke="white" pen="{self.line_width+self.casing}" cap="1" join="1">\n{x1} {y1 + self.casing*((my-y1)/s)} m\n{mx} {my + self.casing*((y1-my)/s)} l\n</path>\n"""
                vis += f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{x1} {y1} m\n{mx} {my} l\n</path>\n"""
                self.verticals.append(vis)
                vis2 = f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{mx} {my} m\n{x2} {y2} l\n</path>\n"""
                self.horizontals.append((vis2))
                vis += vis2
            else:
                s = abs(y2 - my)
                vis = f"""<path stroke="white" pen="{self.line_width+self.casing}" cap="1" join="1">\n{x2} {y2 + self.casing*((my - y2) / s)} m\n{mx} {my + self.casing*((y2 - my) / s)} l\n</path>\n"""
                vis += f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{x2} {y2} m\n{mx} {my} l\n</path>\n"""
                self.verticals.append(vis)
                vis2 = f"""<path {stroke} pen="{self.line_width}" cap="1" join="1">\n{mx} {my} m\n{x1} {y1} l\n</path>\n"""
                self.horizontals.append((vis2))
                vis += vis2
            self.tree_edges[edge] = vis

    def draw_tree(self, output):
        for node in range(self.n_leaves, self.n_nodes):
            r, l = self.adjacency[node]
            y = (self.y_scale * self.RADIUS) * self.get_y_coordinate(node)
            self.add_node(r, y)
            self.add_node(l, y)
            self.add_node(node, y)
            self.add_edge(node, r)
            self.add_edge(node, l)
        self.ipe_drawing(output)

    def ipe_drawing(self, output):
        string_builder = ""
        for e in self.horizontals:
            string_builder += e
        for e in self.verticals:
            string_builder += e
        for n in range(self.n_leaves, self.n_nodes):
            string_builder += self.tree_nodes[n]
        for n in range(0, self.n_leaves):
            string_builder += self.tree_nodes[n]
        X_1, Y_1 = self.x_min-self.RADIUS, self.y_min-self.RADIUS
        X_2, Y_2 = self.x_max+self.RADIUS, self.y_max+self.RADIUS
        string_builder = self.ipe_pre + self.layout.format(X_1, Y_1, X_2, Y_2) + string_builder + self.ipe_post
        with open(output, 'w+') as ipe:
            ipe.write(string_builder)
            ipe.close()
