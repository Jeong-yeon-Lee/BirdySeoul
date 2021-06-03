import React, { useState, useRef, useCallback } from 'react';
import BirdTemplate from './components/BirdTemplate';
import BirdInsert from './components/BirdInsert';
import BirdList from './components/BirdList';
import TodayInsert from './components/TodayInsert';
const App = () => {
  const [todos, setTodos] = useState([
    {
      id: 1,
      text: '쇠청다리도요',
      location: '남동유수지',
    },
    {
      id: 2,
      text: '박새',
      location: '서울대학교',
    },
    {
      id: 3,
      text: '물총새',
      location: '방이습지',
    },
  ]);




  const nextId = useRef(4);
  const onInsert = useCallback(
    (text,location) => {
      const todo = {
        id: nextId.current,
        text,
        location,
      };
      setTodos(todos.concat(todo));
      nextId.current += 1; // nextId 1씩 더하기
    },
    [todos],
  );

  // const onInsert=useCallback(
  //   (location)=>{
  //     const today={
  //       id: nextId.current,
  //       text,
  //       location,
  //     };
  //     setTodays(todays.concat(today));
  //     nextId.current += 1; // nextId 1씩 더하기
      
  //   },
  //   [todays],
  // );

  const onRemove=useCallback(
    id=>{
      setTodos(todos.filter(todo=>todo.id !==id));
    },
    [todos],
  );

  const onToggle=useCallback(
    id=>{
      setTodos(
        todos.map(todo=>
          todo.id===id?{...todo,checked: !todo.checked}:todo,
        )
          );
    
    },
    [todos]
  );

  return (
    <BirdTemplate>
      <BirdInsert onInsert={onInsert} />
      <BirdList todos={todos} onRemove={onRemove}/>
    </BirdTemplate>
  );
};

export default App;
