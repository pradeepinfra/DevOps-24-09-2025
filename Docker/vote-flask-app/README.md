# Vote Flask App ✅

## Build Image
```bash
docker build -t vote-flask-app .
```

## Run Container
```bash
docker run -d -p 5000:5000 --name voteapp vote-flask-app
```

## Access
Open:
http://localhost:5000

## Reset Votes
http://localhost:5000/reset
```
