import React from 'react';
import AuthorList from './components/Author.js'
import axios from 'axios'
import Userlist from './components/User.js'
import { HashRouter, Route, Link, NavLink, BrowserRouter} from 'react-router-dom'


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
      const authors = response.data.results
      this.setState(
        {
          'authors': authors
        }
      )
      console.log('я обновился')
    }).catch(error => console.log(error));

    axios.get('http://127.0.0.1:8000/api/User/').then(response => {
      const users = response.data.results
      this.setState(
        {
          'users': users
        }
      )
    }).catch(error => console.log(error));
  }



  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <a href='/'>Users</a>
              </li>
              <li>
                <a href='/authors'>Authors</a>
              </li>
            </ul>
          </nav>
          <Route exact path='/' component={() => <Userlist users={this.state.users} />} />

          <Route exact path='/authors' component={() => <AuthorList authors={this.state.authors} />} />

        </BrowserRouter>
      </div>
    )
  }
}
export default App;

