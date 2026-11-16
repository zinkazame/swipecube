# Swipe Cube

A 3D Rubik's cube game for Android (and any browser).

## Controls

- **Swipe a face**: touch a side of the cube and drag along it. The row or column you touched turns with your finger and snaps to the nearest quarter turn.
- **Hold, then drag**: press and hold on the cube until it buzzes, then drag to spin the whole cube. Dragging the empty background spins it too.
- **Pinch**: zoom.
- **Cube Types**: Switch seamlessly between 2×2, 3×3, 4×4, and 5×5 cubes at any time.
- **Tutorial Mode**: Complete interactive solving guide for 2×2, 3×3, 4×4, and 5×5 cubes. Browse step-by-step methods, algorithms, and patterns with animated 3D demonstrations, play/pause controls, and move stepping.
- **Buttons**: Cube Type selector (2×2, 3×3, 4×4, 5×5), Scramble, Undo, Solve (auto-solves), Reset, and Tutorial.
- The timer starts on your first move after a scramble. Best times are saved per cube type.

## Get the APK (no Android Studio needed)

1. Create a new GitHub repository and upload everything in this folder (keep `.github/workflows/android.yml`).
2. Open the **Actions** tab, pick **Build Android APK**, and wait for it to finish (about 5 minutes).
3. Download the `swipe-cube-apk` artifact from the run, unzip it, and copy `app-debug.apk` to your phone.
4. Open the file on the phone and allow "Install unknown apps" when asked.

## Build locally with Android Studio

```
npm install
npx cap add android
npx cap sync android
npx cap open android
```

Then press Run in Android Studio. To lock the game to portrait, add
`android:screenOrientation="portrait"` to the `<activity>` tag in
`android/app/src/main/AndroidManifest.xml`.

## Editing the game

The game lives in `src/game.html`. Run `python3 build.py` to regenerate `www/index.html`
(the offline page the app loads), then `npx cap sync android`.

`www/index.html` also works on its own: open it in any browser.
