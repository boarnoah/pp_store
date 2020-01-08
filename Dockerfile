FROM mcr.microsoft.com/dotnet/core/sdk:3.1.100-alpine AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY PPStore/*.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY PPStore ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1.0-alpine
WORKDIR /app

ARG ASPNETCORE_ENVIRONMENT=Staging
ENV ASPNETCORE_ENVIRONMENT ${ASPNETCORE_ENVIRONMENT}

COPY --from=build-env /app/out .

EXPOSE 5000

ENTRYPOINT ["dotnet", "PPStore.dll"]
