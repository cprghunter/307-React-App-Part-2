import React, { Component } from 'react'

const TableBody = props => {
    const rows = props.characterData.map((row, index) => {
        return (
            <tr key={index}>
                <td>{row.name}</td>
                <td>{row.job}</td>
                <td>{row.id}</td>
                <td>
                    <button onClick={() => props.removeCharacter(row.id)}>Delete</button>
                </td>
            </tr>
        )
    })

    return <tbody>{rows}</tbody>
}

const TableHeader = () => {
  return (
    <thead>
      <tr>
        <th>Name</th>
        <th>Job</th>
        <th>Id</th>
      </tr>
    </thead>
  )
}

class Table extends Component {
    render(){
        const { characterData,removeCharacter } = this.props

        return (
            <table>
                <TableHeader />
                <TableBody characterData={characterData} removeCharacter={removeCharacter}/>
            </table>
        )
    }
}

export default Table
             
