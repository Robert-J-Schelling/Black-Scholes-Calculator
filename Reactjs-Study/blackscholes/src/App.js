import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const inputFields = [
    {label:"Start Date", id: "startDate", type:"date",defaultValue:""},
    {label:"End Date", id: "endDate", type:"date",defaultValue:""},
    {label:"Strike Price", id: "strikePrice", type:"number",defaultValue:10000},
    {label:"Spot Price", id: "spotPrice", type:"number",defaultValue:10000},
    {label:"Foreign Interest Rate", id: "foreign_rate", type:"number",defaultValue:0},
    {label:"Domestic Interest Rate", id: "domestic_rate", type:"number",defaultValue:0},
    {label:"Volatility", id: "volatility", type:"number",defaultValue:55},
    {label:"Call/Put", id: "callput",type:"",defaultValue:0},
    {label:"Quantity", id: "quantity", type:"number",defaultValue:5},
    {label:"Premium", id: "premium", type:"number",defaultValue:0},
    {label:"Cashflow", id: "cashflow", type:"number",defaultValue:0},
    {label:"Unit Delta", id: "unit_delta", type:"number",defaultValue:0},
    {label:"Option Delta", id: "option_delta", type:"number",defaultValue:0},
  ]
  return (
    <div className="App">
      <header className="App-header">
        <Clock/>
        <Form inputFields = {inputFields} />
      </header>
    </div>
  );
}

function Form({inputFields}) {
  const [list, setList] = useState([]);

  const handleChildUpdate = (value) => {
      setList(list.concat(value));
    }

    const populateList = (value) => {
      setList(list.concat(value));

    }

  const handleSubmit = (event) => {
    event.preventDefault();

    for (const item in inputFields) {
      populateList(item.id)
    }
    let data = list;

    fetch("http://localhost:5000/result", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    }).then(response => {
      response.json().then(data => {
        console.log("Successful" + data);
      });
    });
  }
  return(
    <div>
      <form onSubmit={handleSubmit}>
        {inputFields.map(field => {
          return(
          <Input label= {field.label} id={field.id} type = {field.type} defaultValue = {field.defaultValue} handleChildUpdate = {handleChildUpdate}/>
          );
        })}
        <input type="submit" value="Submit"/>
      </form>
    </div>
  );
}

function Input({handleChildUpdate,label,id,type,defaultValue}) {
  const[value,setValue] = useState(defaultValue)

  const handleChange = (event) => {
    const element = event.target;
    setValue(element.value)
    handleChildUpdate({value,id})
  }


  if (id === "callput") {
    return (
      <div>
      <label>{label + "  "}</label>
      <select id={id}>
        <option value="call">Call</option>
        <option value="put">Put</option>
      </select>
      </div>
    );
  }
  else{
    return(
      <div>
      <label>{label + "  "}</label>
      <input id = {id} type={type} value = {value} onChange = {handleChange}></input>
      </div>
    );
  }
}

function Clock() {
  const [time, setTime] = useState(new Date())

  useEffect(() => {
    const timerID = setInterval(() => {
      setTime(new Date())
    }, 1000);

    return function cleanup() {
      clearInterval(timerID);
    };
  });

  return (
    <div>
      <h2>{time.toLocaleTimeString()}.</h2>
    </div>
  );

}

export default App;
