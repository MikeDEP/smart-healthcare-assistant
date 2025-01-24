# Use official Node.js image from Docker Hub
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json for dependencies installation
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all the source code
COPY . .

# Expose the port React app runs on (usually 3000)
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
