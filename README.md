# GIF Background for i3
> Everyone wants live / gif wallpapers right?

![showcase.gif](showcase.gif)

# Dependencies
> These are the dependencies:
* feh

# Install
> To install this, follow these steps:

## Edit the service file
> First, edit the `gifbg.service` file to match the path where you placed
> this source code, and change `User=ianertson` to your username.

## Move the service file
> Now, you will have to move the service file to:

    cp gifbg.service /etc/systemd/system/.

## Create a directory for the wallpaper
> `gifbg` needs a directory in your `$HOME` directory, create a directory
> there like this:

    mkdir ~/.gifbg


## Set your wallpaper
> Download a `.gif` of your choice and place it in `~/.gifbg`

## Split your gif
> Now we need to split the gif into multiple `.pngs`, use `ImageMagick`
> for this:

    convert yourgif.gif target.png

> NOTE: the last argument needs to be `target.png`, exactly like this.  
> You should now have some files in `~/.gifbg` looking like this:

    target-0.png   target-13.png  target-17.png  target-20.png  target-24.png  target-28.png  target-4.png  target-8.png
    target-10.png  target-14.png  target-18.png  target-21.png  target-25.png  target-29.png  target-5.png  target-9.png
    target-11.png  target-15.png  target-19.png  target-22.png  target-26.png  target-2.png   target-6.png
    target-12.png  target-16.png  target-1.png   target-23.png  target-27.png  target-3.png   target-7.png

> Good job!

## Start the gifbg service
> Lets get those pixels moving!! start the service:

    systemctl start gifbg

> Your wallpaper should be moving now!

# Troubleshooting
> If your having problems, this command is pretty useful to see errors:

    journalctl -u gifbg
