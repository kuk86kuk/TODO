import React from "react"


const UserItem = ({ user }) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const Userlist = ({users}) => {
    return (
        <div>
            <h2>Users</h2>
            <table>
                
                <th>
                    First name
                </th>

                <th>
                    Last Name
                </th>
                <th>
                    email
                </th>
                {users.map((user) => <UserItem user={user} />)}
            
            </table>
        </div>
    )
}


export default Userlist