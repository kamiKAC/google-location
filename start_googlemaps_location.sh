docker run -d --name googlemaps_location  -v ./:/files -e GOOGLE_EMAIL="example_email@gmail.com" --restart unless-stopped --memory="50m" --memory-swap="50m" --cpus="0.5" google_location