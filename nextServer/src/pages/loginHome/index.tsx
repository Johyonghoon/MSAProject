import { NextPage } from "next"
import { useEffect, useState } from "react";
import styled from 'styled-components';
import { useDispatch, useSelector } from 'react-redux';
import { User } from "@/modules/types"
import { AppState } from "@/modules/store"
import {userSelector} from "@/modules/slices";
import {useAppSelector} from "@/modules/store";

interface Props{ article: string }

const LoginHomePage: NextPage<Props> = () => {

  const [user, setUser] = useState({
    user_id : '',
    user_email : '',
    password : '',
    user_name : '',
    phone : '',
    birth : '',
    address : '',
    job : '',
    user_interests : '',
    token : '',
    created_at : '',
    updated_at : ''
  }) 
    /**const [token, setToken] = useState('')*/
  //const userData: string = useSelector(userSelector)
  //const result: string = useAppSelector((state: AppState) => state.user.token || 'tess')
  // useEffect(()=>{
  //   alert(`6 session is ${localStorage.getItem("session")}`)
  //   const session:{
  //     user_id : '',
  //     user_email : '',
  //     password : '',
  //     user_name : '',
  //     phone : '',
  //     birth : '',
  //     address : '',
  //     job : '',
  //     user_interests : '',
  //     token : '',
  //     created_at : '',
  //     updated_at : ''
  //   } = JSON.parse(localStorage.getItem("session")||'{}')
  //   setUser(session)
  // },[])


  return (<>
        
      <Sheet >
        <thead>
          <Row>
            <Cell colSpan={2}><h6>회원정보 </h6></Cell>
          </Row>
        </thead>
        <tbody>
          <Row>
            <Cell>
              <label htmlFor="user_email">이메일(ID)</label></Cell>
            <Cell> 
              {user.user_email}
            </Cell>
          </Row>
        <Row><Cell>
      <label htmlFor="password">비밀번호</label></Cell>
      <Cell>
            </Cell>
          </Row>
         
          <Row>
            <Cell>
              <label htmlFor="user_name">이름(실명)</label>
            </Cell>
            <Cell>
           
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="phone">전화번호</label></Cell>
            <Cell>
            
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="birth">생년월일</label> </Cell>
            <Cell>
              
            </Cell>
          </Row>
          <Row>
            <Cell><label htmlFor="address">주소</label></Cell>
            <Cell></Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="job">직업</label></Cell>
            <Cell>
            </Cell>
          </Row>
          <Row>
            <Cell>
            <label htmlFor="user_interests">관심사항</label></Cell>
            <Cell>
            </Cell>
          </Row>
          
          <Row>
            <Cell colSpan={2}><button type="submit" >수정하기</button></Cell>
          </Row>
          
        </tbody>
      </Sheet>

      
    </>)

}

const Sheet = styled.table`
border: 1px solid black
width: 70%
`
const Row = styled.tr`
border: 1px solid black
`
const Cell = styled.td`
border: 1px solid black,
`
const Input = styled.input`
width: 100%
`

export default LoginHomePage