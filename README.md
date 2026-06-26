# Monte Carlo Integration

Estimates the volume of a 3D solid — equivalently, approximates a double integral — using the Monte Carlo method.

## What it does

Given a solid in 3D space defined by:

- an **(x, y) region** bounded by four boundary functions (`f_left`, `f_right`, `f_front`, `f_back`), and
- a **ceiling** and a **floor** function `f(x, y) → z`,

the program randomly samples points inside a bounding box (called the *restriction cube*) and counts the fraction that fall inside the solid. That fraction, multiplied by the bounding box volume, gives the estimated volume of the solid (i.e. the value of the double integral).

### Example (as shipped)

Estimates the integral of `(1/2) * x * (1 + y)` over the unit square `[0,1] × [0,1]` (floor at `z = 0`). The analytic result is `1/4`.

## Algorithm

```
volume ≈ (points inside solid / total points) × volume of restriction cube
```

1. Construct a *restriction cube* that fully contains the solid.
2. Draw `n` random points uniformly inside the cube.
3. For each point, test membership: is `(x, y)` in the region **and** `f_floor(x,y) ≤ z ≤ f_ceiling(x,y)`?
4. Return `(hits / n) × cube_volume`.

Accuracy improves as `n` grows (error ~ `1/√n`).

## Dependencies

| Package | Purpose |
|---------|---------|
| `numpy` | Vectorised random point generation |
| `tqdm`  | Progress bar for the sampling loop |

Install with:

```bash
pip install numpy tqdm
```

`math` is from the Python standard library and requires no installation.

## How to run

```bash
python monte_carlo_integration.py
```

The script prints the estimated volume to stdout after completing all iterations.

### Adjusting parameters

Edit `monte_carlo_integration.py` directly:

| Variable / function | What to change |
|---------------------|----------------|
| `n_points`          | Number of random samples (default `1 000 000`) |
| `restriction`       | Bounding box `(x_min, x_max), (y_min, y_max), (z_min, z_max)` |
| `f_left`, `f_right`, `f_front`, `f_back` | (x, y) region boundary functions |
| `f_ceiling`, `f_floor` | Upper and lower surface functions `f(x, y)` |
