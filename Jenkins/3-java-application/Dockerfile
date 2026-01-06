# Use lightweight Java 21 runtime
FROM eclipse-temurin:21-jre-alpine

# Set working directory inside container
WORKDIR /app

# Copy executable JAR from Maven build
COPY target/java-application-1.0.jar app.jar

# Run the application
CMD ["java", "-jar", "app.jar"]
