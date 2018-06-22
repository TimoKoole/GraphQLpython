# GraphQLpython
Use mocked mongo db, no mongo needed.
Install packages with 

    pip install -r requirements.txt


# Examples
## Search
    query{
      regelingen(status:"Actief"){
        edges{
          node{
            regelingNaam
          }
        }        
      }
    }
    
## Find all  
    query{
      regelingen{
        edges{
          node{
            regelingNaam
            regelingWaardes{
              franChise
              PPtoegestaan
            }
            
          }
        }
        
      }
    }