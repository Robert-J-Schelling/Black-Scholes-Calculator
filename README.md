# Black-Scholes-Calculator
After pulling the Image you can run it in the cmd with the following command:

  macOS: 
    docker run --rm -ti -e DISPLAY=docker.for.mac.host.internal:0 Tag Name
  
  Windows:
    docker run --rm -ti -e DISPLAY=host.docker.internal:0 Tag Name
  
   **If there is is an error you will have to install Xming https://sourceforge.net/projects/vcxsrv/
  
  Linux:
   docker run --rm -ti --net=host -e DISPLAY=:0 Tag Name
  
