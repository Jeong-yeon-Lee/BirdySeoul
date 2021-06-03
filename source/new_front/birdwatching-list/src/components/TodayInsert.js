import React, { useState, useCallback } from 'react';
import { MdAdd } from 'react-icons/md';
import './TodayInsert.scss';

//새로운 항목 입력 및 추가 
//state를 통해 인풋의 상태 관리 

const TodayInsert = ({ onInsert }) => {
  const [value2, setValue] = useState('');
  const onChange = useCallback((e) => {
    setValue(e.target.value2);
  }, []);

  const onClick = useCallback(
    (e) => {
      onInsert(value2);
      setValue('');

      e.preventDefault(); //페이지새로고침 방지
    },
    [onInsert, value2],
  );

  return (
    <form className="TodayInsert" >
      <input
        placeholder="어디에서 관찰했나요?"
        value={value2}
        onChange={onChange}
      />
      {/* <button type="button" onClick={onClick}>
        <MdAdd />
      </button> */}
    </form>
  );
};

export default TodayInsert;
