# pp_store
Customer storefront for Pannucis Pizza


### Notes
1. Installl .NET Core 3.1 SDK
2. Install dependencies

       dotnet restore
       
3. Run

       dotnet run
       
       
#### Deployment / Dev with Docker
1. Install docker
2. Build container

       docker build -t PPStore:latest .
       
3. Run container

       docker run -p 5000:5000 --name ppstore_c PPStore
       
#### Deployment AWS
Deploy to ECR -> ECS 