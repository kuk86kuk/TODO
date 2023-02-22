import React from 'react';
import AuthorList from './components/Author.js'
import axios from 'axios'
import Userlist from './components/User.js'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': [],
      'users': []
    }
    
    
  }
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/authors/').then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors
          }
        )
      }).catch(error => console.log(error));

      axios.get('http://127.0.0.1:8000/api/User/').then(response => {
        const users = response.data
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error));
  }



  render() {
    return (
      <div>
        <div>
          <AuthorList authors={this.state.authors} />
        </div>
        <hr></hr>
        <div>
          <Userlist users={this.state.users} />
        </div>
      </div>
    )
  }
}
export default App;

