# 🌸 Anime Academy — Smart Classroom Digital Twin

### Computer Graphics Microproject

**Project Topic:** Digital Twin of a Smart Classroom with Multiple Views using Orthographic Projection

---

## 📌 Project Overview

**Anime Academy — Smart Classroom Digital Twin** is an interactive Computer Graphics microproject that creates a 3D mathematical representation of a smart classroom and displays it through multiple orthographic views.

The project combines fundamental Computer Graphics concepts with an anime-inspired classroom design, creating an engaging way to understand 3D object representation, coordinate systems, geometric transformations, orthographic projection, and rendering.

The same 3D classroom model can be viewed from four different perspectives:

- Front Orthographic View
- Top Orthographic View
- Side Orthographic View
- Isometric Orthographic View

---

## ✨ Features

- 🏫 Interactive 3D smart classroom representation.
- 📐 Four different orthographic projection views.
- 🖥️ Smart board and projector representation.
- 🪑 Teacher desk and multiple student desks.
- 💻 Computer monitors and classroom equipment.
- 🚪 Doors and windows.
- 🌸 Anime-academy-inspired visual elements.
- 📊 Digital twin status dashboard.
- 🔍 Interactive object selection.
- 📏 Object dimensions and coordinate display.
- 🔲 Toggleable grid and dimensions.
- 🔎 Zoom controls for better visualization.

---

## 🎨 Classroom Components

The digital classroom includes the following geometric objects:

| Component | Representation |
|---|---|
| Classroom structure | 3D cuboids |
| Smart board | Rectangular cuboid |
| Teacher desk | Desk and supporting cuboids |
| Student desks | Multiple geometric objects |
| Computer monitors | Rectangular cuboids |
| Projector | 3D geometric object |
| Door | Rectangular surface |
| Windows | Rectangular surfaces |
| Decorations | Additional geometric elements |

---

## 🧠 Computer Graphics Concepts Implemented

### 1. 3D Coordinate System

Every object in the classroom is represented using three-dimensional coordinates.

- **X-axis:** Left and right movement.
- **Y-axis:** Vertical movement or height.
- **Z-axis:** Front and back movement.

Example:

```text
Desk Center = (3, 1, 2)
```

### 2. Geometric Object Representation

Most classroom components are represented using cuboids.

A cuboid consists of:

- 8 vertices
- 12 edges
- 6 faces

The vertices define the object's geometry, while the edges connect the vertices to form its structure.

### 3. Orthographic Projection

Orthographic projection converts 3D coordinates into 2D screen coordinates without perspective division.

The project implements four different views.

**Front View**

```text
screen_x = X
screen_y = Y
```

**Top View**

```text
screen_x = X
screen_y = -Z
```

**Side View**

```text
screen_x = Z
screen_y = Y
```

**Isometric-Style Orthographic View**

```text
screen_x = (X - Z) * cos(30°)

screen_y = Y - (X + Z) * sin(30°)
```

These equations allow the same 3D classroom model to be displayed in different 2D representations.

### 4. Rendering

After calculating the projected 2D coordinates, the application renders the geometric objects on the screen using Pygame.

### 5. Multiple View Representation

The project demonstrates how a single 3D model can be represented through multiple orthographic views for better spatial understanding.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Pygame | Graphics rendering and interaction |
| Mathematics | Projection calculations |
| 3D Coordinate Geometry | Object representation |
| Orthographic Projection | Conversion from 3D to 2D |

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have:

- Python 3.10 or later
- pip package manager

### Step 1: Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### Step 2: Navigate to the Project Folder

```bash
cd anime-academy
```

### Step 3: Install Dependencies

```bash
python -m pip install pygame
```

### Step 4: Run the Application

```bash
python main.py
```

**For Windows users:**

```bash
py main.py
```

---

## 🎮 Application Controls

| Key | Function |
|---|---|
| `1` | Switch to Front View |
| `2` | Switch to Top View |
| `3` | Switch to Side View |
| `4` | Switch to Isometric View |
| `TAB` | Select Next Object |
| `+` | Zoom In |
| `-` | Zoom Out |
| `R` | Reset Zoom |
| `G` | Toggle Grid |
| `D` | Toggle Dimensions |
| `H` | Toggle Help Screen |
| `ESC` | Exit Application |

---

## 📊 Digital Twin Dashboard

The application includes a simulated smart classroom monitoring dashboard.

Example classroom status:

| Parameter | Simulated Value |
|---|---|
| Occupancy | 28 Students |
| Temperature | 24°C |
| Lighting | 72% |
| Projector | ONLINE |
| Smart Board | ONLINE |

**Note:** These values are simulated for demonstration purposes. The current implementation does not use real IoT sensors.

In future versions, real-time sensor data can be integrated to monitor the physical classroom environment.

---

## 🎬 Project Demonstration

Follow these steps to demonstrate the application during the project review:

1. Launch the application.
2. Start with the Isometric View by pressing `4`.
3. Explain the 3D classroom representation.
4. Press `1` to demonstrate the Front View.
5. Press `2` to demonstrate the Top View.
6. Press `3` to demonstrate the Side View.
7. Press `4` to return to the Isometric View.
8. Press `TAB` to select different classroom objects.
9. Demonstrate object coordinates and dimensions.
10. Press `G` to toggle the grid.
11. Press `D` to toggle dimensions.
12. Press `H` to display the help screen.

---

## 🎤 Project Explanation

**Presentation Introduction:**

"My project is an interactive digital twin of an anime-themed smart classroom. The classroom is represented as a 3D collection of geometric objects using X, Y, and Z coordinates.

I implemented orthographic projection to convert the 3D model into four different 2D views: Front, Top, Side, and Isometric.

The project demonstrates important Computer Graphics concepts, including 3D coordinate systems, geometric object representation, vertices, edges, orthographic projection, and rendering.

The anime-academy theme provides the visual identity, while the underlying implementation focuses on the mathematical and graphical concepts."

---

## 🚀 Future Enhancements

The following features can be implemented in future versions:

- Integration with real IoT sensors.
- Real-time classroom temperature monitoring.
- Real-time student occupancy detection.
- Mouse-based object selection.
- Interactive camera rotation.
- OpenGL-based 3D rendering.
- Blender 3D model integration.
- Collision detection.
- Emergency and evacuation simulation.
- Screenshot capturing functionality.
- Interactive floor-plan measurements.

---

## ❓ Viva Questions and Answers

**Q1. What is Orthographic Projection?**

Orthographic projection is a graphical projection technique in which parallel projection lines are used to represent a 3D object on a 2D plane. Object size does not change with depth.

**Q2. Why are multiple views required?**

Multiple views help understand an object's dimensions and spatial arrangement from different directions.

**Q3. What is a Digital Twin?**

A digital twin is a digital representation of a physical object, environment, or system.

**Q4. Why did you use Python?**

Python provides simple syntax and supports rapid development. Pygame provides the graphics rendering and interaction layer.

**Q5. What is a Vertex?**

A vertex is a point in 3D space represented using X, Y, and Z coordinates.

**Q6. What is Wireframe Representation?**

Wireframe representation displays an object using its vertices and connecting edges rather than fully rendered surfaces.

**Q7. What is the difference between Orthographic and Perspective Projection?**

Orthographic projection preserves the apparent size of objects regardless of depth, whereas perspective projection makes distant objects appear smaller.

**Q8. What is the main Computer Graphics concept implemented?**

The main concept is orthographic projection, which transforms 3D coordinates into 2D screen coordinates using mathematical equations.

---

## 📚 Project Workflow

```text
       3D Coordinates
              |
              v
      Geometric Objects
              |
              v
       Vertices & Edges
              |
              v
    Orthographic Projection
              |
              v
        2D Coordinates
              |
              v
          Rendering
              |
              v
       Multiple Views
```

---

## 🎯 Academic Relevance

Although the project uses an anime-inspired theme, its primary objective is to demonstrate the fundamentals of Computer Graphics.

The implementation focuses on:

- 3D coordinate systems.
- Geometric object construction.
- Vertex and edge representation.
- Mathematical projection equations.
- Orthographic projection.
- 2D rendering.
- Multiple-view visualization.

The project demonstrates how mathematical concepts can be applied to create an interactive graphical representation of a real-world environment.

---

## 👩‍💻 Project Information

**Project Name:** Anime Academy — Smart Classroom Digital Twin

**Subject:** Computer Graphics

**Project Type:** Academic Microproject

**Topic:** Digital Twin of a Smart Classroom with Multiple Views using Orthographic Projection

**Programming Language:** Python

**Graphics Library:** Pygame

---

<p align="center">
  🌸 <b>Anime Academy — Where Computer Graphics Meets Creativity!</b> 🌸
</p>
