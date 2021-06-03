import React, { useState, useCallback } from 'react';
import { MdAdd } from 'react-icons/md';
import './BirdInsert.scss';
import TodayInsert from './TodayInsert';

//새로운 항목 입력 및 추가 
//state를 통해 인풋의 상태 관리 

const BirdInsert = ({ onInsert }) => {
  const [value, setValue] = useState('');
  const onChange = useCallback((e) => {
    setValue(e.target.value);
  }, []);
  const onSubmit = useCallback(
    (e) => {
      onInsert(value);
      setValue('');

      e.preventDefault(); //페이지새로고침 방지
    },
    [onInsert, value],
  );


  return (
    <form className="BirdInsert" onSubmit={onSubmit}>
      <input placeholder="어디서 관찰했나요?"
      value={value2}
      onChange={onChange2}
      ></input>
      <input
        placeholder="오늘 본 새를 기록하세요!"
        value={value}
        onChange={onChange}
      />
      <button type="submit">
        <MdAdd />
      </button>
    </form>
  );
};

export default BirdInsert;
