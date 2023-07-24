# badappleroblox
[play here](https://www.roblox.com/games/14171404293/bad-apple-but-its-roblox)
and a small tutorial if u wanna run it urself or with another video
### requirements
- [python](https://www.python.org/)
- [Pillow](https://pypi.org/project/Pillow/)
- [ffmpeg](https://www.ffmpeg.org/)
### how to setup
1. open terminal on the repository's directory
2. extract the frames of your video to the `/frames` folder with the command: `ffmpeg -i (input) frames\%01d.png` (change the `\` to `/` if ur on linux)
3. install pillow with `pip install Pillow` or `python3 -m pip install Pillow` (if ur on linux)
4. change the fps value inside the `main.py` file
5. run the program with `py main.py` and wait until all batches and data are dumped
6. publish the `output` directory somewhere online so the game can read it (recommendation is that you use github like me lol)
7. IF your video has a different scale, create a canvas of studs like the one in game, each model represents the X axis, each stud represents the Y axis, you can run this script that i used to make the screen on the command bar:
```lua
local videoWidth = 0
local videoHeight = 0
--[[ make sure to change the 2 values above ]]
local counter = 0
local screen = Instance.new("Model")
local axis0 = Instance.new("Model")
screen.Name = "Screen"
axis0.Name = "0"
while counter < videoHeight do
    local part = Instance.new("Part") 
    part.Position = Vector3.new(0, counter, 0)
    part.Name = tostring((videoHeight - 1) - part.Position.Y)
    part.Color = Color3.new(0, 0, 0)
    part.Anchored = true
    part.CanCollide = false
    part.CastShadow = false
    part.Material = Enum.Material.SmoothPlastic
    part.Size = Vector3.new(1, 1, 1)
    if not axis0:FindFirstChild(part.Name) then
        part.Parent = axis0
    else part:Destroy() end
    counter += 1
end
axis0.Parent = screen
counter = 0
while counter < videoWidth do
    local axisX = axis0:Clone()
    axisX.Name = tostring(counter)
    for _, v in pairs(axisX:GetChildren()) do
        v.Position += Vector3.new(-counter, 0, 0)
    end
    if not screen:FindFirstChild(axisX.Name) then
        axisX.Parent = screen
    else axisX:Destroy() end
    counter += 1
end
screen.Parent = workspace
```