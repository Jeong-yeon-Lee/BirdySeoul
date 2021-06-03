import React from 'react';
import {
  MdCheckBoxOutlineBlank,
  MdCheckBox,
  MdRemoveCircleOutline,
} from 'react-icons/md';
import cn from 'classnames';
import './BirdListItem.scss';

const BirdListItem = ({ todo, onRemove}) => {
  const { id, text, location} = todo;
  return (
    <div className="BirdListItem">
     
        <div className="text">{text}----------@{location}</div>
        
      
      <div className="remove" onClick={()=>onRemove(id)}>
        <MdRemoveCircleOutline />
      </div>
    </div>
  );
};

export default BirdListItem;
