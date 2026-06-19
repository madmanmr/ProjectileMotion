# Projectile Motion Game

A Python/Pygame game that combines projectile motion physics with a target shooting challenge.

The project started as a projectile motion simulator and later evolved into a game where the player must hit a target using physics calculations.

---

## Features

- Real-time projectile motion simulation
- Adjustable:
  - Gravity
  - Initial velocity
  - Launch angle
- Displays:
  - Distance travelled
  - Height
  - Speed
  - Flight time
  - Maximum height
- Random target generation
- Scoring system
- Limited shots
- Aim Assist mode
- Game Over screen
- Restart functionality

---

## Controls

### Variable Controls

| Control | Function |
|----------|----------|
| + Gravity | Increase gravity |
| - Gravity | Decrease gravity |
| + Velocity | Increase launch velocity |
| - Velocity | Decrease launch velocity |
| + Angle | Increase launch angle |
| - Angle | Decrease launch angle |

### Game Controls

| Button | Function |
|---------|----------|
| Start | Fire projectile |
| Restart | Generate a new target |
| Aim Assist | Shows predicted trajectory |

---

## Scoring

| Target Ring | Points |
|------------|--------|
| Bullseye | 50 |
| Middle Ring | 30 |
| Outer Ring | 10 |

When Aim Assist is enabled:

| Target Ring | Points |
|------------|--------|
| Bullseye | 25 |
| Middle Ring | 15 |
| Outer Ring | 5 |

---

## Physics Used

### Horizontal Motion

```python
x = v₀ cos(θ)t
```

### Vertical Motion

```python
y = v₀ sin(θ)t - ½gt²
```

### Maximum Height

```python
H = (v₀ sin(θ))² / (2g)
```

### Range

```python
R = (v₀² sin(2θ)) / g
```

### Flight Time

```python
T = (2v₀ sin(θ)) / g
```

---

## Requirements

Install dependencies:

```bash
pip install pygame numpy
```

Run:

```bash
python main.py
```

---

## Development Log

### 14/06/26 – Planning & Physics
- Revised projectile motion equations.
- Set up the Pygame window and project structure.
- Implemented the core projectile motion calculations.

### 15/06/26 – User Interface
- Added buttons and variable displays.
- Fixed timing issues so the simulation matched theoretical flight times.
- Added an end screen and restart system.

### 16/06/26 – Refactoring & Bug Fixes
- Reorganised the code structure.
- Fixed several timing and display bugs.
- Improved variable updates and restart functionality.

### 17/06/26 – Game Features
- Added a randomly positioned target.
- Added projectile splash effects.
- Implemented collision detection.
- Created a multi-zone scoring system.
- Added an aiming line.

### 18/06/26 – Aim Assist
- Added a trajectory prediction parabola.
- Introduced a score penalty when aim assist is enabled.
- Improved the overall UI layout.

### 19/06/26 – Final Polish
- Improved button and screen layouts.
- Added a Game Over screen.
- Added final score display and Play Again button.
- Fixed remaining bugs and completed the project.

---

## Features

- Adjustable launch velocity
- Adjustable launch angle
- Adjustable gravity
- Accurate projectile motion physics
- Random target placement
- Multi-zone scoring system
- Splash effects
- Aim assist trajectory prediction
- Live flight statistics
- Restart functionality
- Game Over screen

---

## What I Learned

- Projectile motion physics
- Pygame development
- Collision detection
- Real-time simulation
- UI design
- Debugging and refactoring

---

## Future Improvements

- Moving targets
- Wind resistance
- Multiple levels
- High score system
- Different target types
- Better graphics
- Sound effects
- Power meter

---

## Final Thoughts

Write a short reflection here about what went well, what was difficult, and what you would improve if you rebuilt the project.








