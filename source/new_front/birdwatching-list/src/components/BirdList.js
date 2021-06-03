import React from 'react';
import BirdListItem from './BirdListItem';
import './BirdList.scss';

const BirdList = ({ todos, onRemove, onToggle }) => {
  return (
    <div className="BirdList">
      {todos.map(todo => (
        <BirdListItem todo={todo} key={todo.id} onRemove={onRemove} onToggle={onToggle}/>
      ))}
    </div>
  );
};

export default BirdList;
