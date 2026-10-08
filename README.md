## Q2: WebXR

```bash
python -m http.server 8002 --directory Q2
```

Open http://localhost:8002/ and click "Enter AR".

## Q3: Camera Projection

```bash
python Q3/projection.py
```
You can edit the values in the `main` block to change the camera parameters or input point. 
## Q4: Phong Shading

```bash
python -m http.server 8004 --directory Q4
```

Open http://localhost:8004/ to view the final two-light scene.

To run individual parts, You can paste the contents of `Q4/4a.js`, `4b.js`, or `4c.js` into the JavaScript editor at [Babylon.js Playground](https://playground.babylonjs.com/) and click "Run". 
