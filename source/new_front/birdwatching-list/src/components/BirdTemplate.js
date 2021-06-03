import React from 'react';
import './BirdTemplate.scss';


//children으로 내부 JSX를 props로 받아와서 렌더링

const BirdTemplate = ({ children }) => {
  return (
    <div className="BirdTemplate">
      <div className="app-title">오늘의 야장</div>
      <div className="content">{children}</div>
    </div>
  );
};

export default BirdTemplate;
