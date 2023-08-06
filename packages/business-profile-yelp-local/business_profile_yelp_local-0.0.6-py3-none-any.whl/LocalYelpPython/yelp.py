from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def get_data(business_type, location):
  api_endpoint = 'https://api.yelp.com/v3/graphql'
  api_key = 'wkq-K87ISpTHLQncV1LbKztKCC1oGjnYIsnHMZtX5Mm3P6oM8X3NTyB8_mDAsPIj8KekzwNQCpMVemTi-yQ9HmVvTAOO02dW5b6mXQlVlKOKyg0cF0KRWmEYSDhJZHYx'


  query = gql('''
    query ($term: String!, $location: String!, $limit: Int!, $offset: Int!) {
      search(term: $term, location: $location, limit: $limit, offset: $offset) {
        business {
          name
          rating
          location {
            address1
            city
            state
            country
            postal_code
            address2
            address3
            formatted_address
          }
          distance
          phone
          photos
          price
          coordinates {
            latitude
            longitude
          }
          id
          alias
          categories {
            alias
            title
          }
          display_phone
          hours {
            hours_type
            is_open_now
            open {
              day
              is_overnight
              end
              start
            }
          }
          is_claimed
          is_closed
          messaging {
            url
            use_case_text
          }
          review_count
          reviews {
            user {
              id
              image_url
              name
              profile_url
            }
            id
            rating
            text
            time_created
            url
          }
          special_hours {
            start
            is_overnight
            is_closed
            end
            date
          }
        }
      }
    }
  ''')

  # Define GraphQL transport
  transport = RequestsHTTPTransport(
      url=api_endpoint,
      headers={'Authorization': f'Bearer {api_key}'},
      use_json=True,
  )

  # Define GraphQL client
  client = Client(
      transport=transport,
      fetch_schema_from_transport=True,
  )

  limit = 50
  offset = 0
  data = []

  while offset < limit:
      try: 
        response = client.execute(query, variable_values={'term': business_type, 'location': location, 'limit': limit, 'offset': offset})

        for business in response['search']['business']:
            data.append(business)

        offset += limit
      
      except Exception as e:
        return f"Exception occurred: {str(e)}"

  return data
