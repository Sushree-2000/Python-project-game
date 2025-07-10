1) What is **dangling image** in Docker? (Or Why is Docker creating multiple <none> images?)
When you rebuild an image using:

<!-- bash -->
docker build -t python-proj-game-ml .

...but the previous image (with the same tag) is still being used by a container, Docker cannot delete the old one.
So it orphanizes the older image by removing the tag, showing it as:

REPOSITORY             TAG       IMAGE ID
<none>                 <none>    <image_id>

These are called **"dangling images"** — they’re just older layers without names now.

<!-- # Remove all dangling images -->
docker image prune -f          