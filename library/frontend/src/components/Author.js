import React from 'react'



const AuthorItem = ({ author }) => {
    return (
        <tr>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({ authors }) => {
    return (
        <div>
            <h2>Authors</h2>
            <table>
                <th>
                    First name
                </th>

                <th>
                    Last Name
                </th>

                <th>
                    Birthday year
                </th>

                {authors.map((author) => <AuthorItem author={author} />)}
            </table>
        </div>
    )
}
export default AuthorList
