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

# Development Log

Use this section to record the process of making the project.

---

## Day 1 - Initial Planning

Date:

Notes:









---

## Day 2 - Projectile Physics

Date:

Notes:









---

## Day 3 - UI and Controls

Date:

Notes:









---

## Day 4 - Target System

Date:

Notes:









---

## Day 5 - Scoring System

Date:

Notes:









---

## Day 6 - Aim Assist

Date:

Notes:









---

## Day 7 - Game Over Screen

Date:

Notes:









---

## Bugs Encountered

| Bug | Cause | Fix |
|------|--------|-----|
| | | |
| | | |
| | | |
| | | |

---

## Things I Learned

- 
- 
- 
- 
- 

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








