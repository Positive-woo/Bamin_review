from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import google.generativeai as genai
import os
import sys
## ETC import
import time
from tkinter import messagebox
import tkinter as tk



## 개인정보
id = 'kjs604500'
pw = '1212kjs!'
store_code = '14247040'
GOOGLE_API_KEY= "AIzaSyCnLGOrmzp-iTeQx08vJYN6jH_5h1U3Q0s"




def main():
    options = Options()
    options.add_argument('--window-size=1000,900')
    options.add_argument('--window-position=0,0')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = options)
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    
    # URL 접속
    url = "https://self.baemin.com/bridge"
    driver.get(url)  # 접속
    action = ActionChains(driver)
    
    #로그인 화면 접속
    try:
        # 요소가 나타날 때까지 최대 10초 대기
        # 로그인 창 입장
        login_button_1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.button.small.self-ds'))
        )
        login_button_1.click()
        #ID 칸 클릭 후 id 넣기
        ID_blank = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="id"]'))
        )
        ID_blank.click()
        action.click(ID_blank).send_keys(id).perform()
        #PW 칸 클릭 후 PW 넣기
        PW_blank = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
        )
        PW_blank.click()
        action.click(PW_blank).send_keys(pw).perform()
        #로그인 클릭
        login_button_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Button__StyledButton-sc-1cxc4dz-0.hlLPsc'))
        )
        login_button_2.click()
    except Exception as e:
        print(f"1단계 요소를 찾을 수 없습니다: {e}")
        sys.exit(0)
    
    #3초 쉬기
    os.system('cls')
    time.sleep(1)
    
    # 가게 고유 넘버 없이 리뷰 페이지로 이동
    try:
        review_url = "https://self.baemin.com/shops/" + store_code +"/reviews"  # 가게 고유 넘버 없이 리뷰 페이지로 이동하는 URL
        driver.get(review_url)
        print("리뷰 페이지로 이동했습니다.")
    except Exception as e:
        print(f"리뷰 페이지로 이동할 수 없습니다: {e}")
        sys.exit(0)
    
    def ad_pop_no_answer():
        # 광고창 끄기
        try:
            ad_popup = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.bsds-modal-header-button-wrapper'))
            )
            if ad_popup:
                print("광고 팝업이 감지되었습니다.")
                # 닫기 버튼 클릭 (필요한 버튼의 정확한 CSS 셀렉터 사용)
                no_see_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "bsds-button") and contains(@class, "css-a2ehx")]'))
                )
                no_see_button.click()
                print("광고 팝업을 1일간 보지 않기로 설정했습니다.")
        except Exception as e:
            print("광고 팝업이 없습니다: ")
        
        #미답변 클릭
        try:
            # "미답변" 텍스트를 포함하는 div 요소 클릭
            no_answer = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "미답변")]'))
            )
            no_answer.click()
            print("미답변을 클릭했습니다.\n\n\n\n")
        except Exception as e:
            print(f"미답변을 클릭하지 못했습니다. {e}")
            sys.exit(0)
            
    ad_pop_no_answer()
    
    ###-----------------------반복문 입장----------------------------###
    ###-----------------------반복문 입장----------------------------###
    ###-----------------------반복문 입장----------------------------###
    
    def loop_answer():
        while True:
            os.system('cls')
            print("------------------------------------------------------------")
            again = input("다음 답글을 등록하시겠습니까? 1 = yes, 0 = no: \n")
            if again == '1':
                #리뷰내용가져오기
                try:
                    review_content = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'p.review-cont'))
                    )
                    review_text = review_content.text
                except Exception as e:
                    print(f"리뷰 내용을 가져올 수 없습니다: {e}")
                
                
                setted_response = "너는 이제 20대 남성이야. 배달 전문 횟집 사장님이야(전부 배달의 리뷰). 이 리뷰에 대한 답글을 4줄 정도로 짧게 대답해줘. 말투는 담백하게 감탄사 빼고 \n" + review_text
                
                ### 리뷰에 들어갈 문장으로 정제하기
                
                response = model.generate_content(setted_response)
                pin_text = """
    
                
    숙성회136은 맛있는 음식, 정갈한 담음새, 그리고 고객 만족을 위해서 최선을 다하고 있습니다.
    
    ㅁ맛있는 음식을 만들기 위해 숙성회136은 인천 연안부두와 노량진 수산시장, 각종 해산물 산지 공급 업체와의 긴밀한 협력으로 수산물이 제일 신선할 때 사용합니다.
    
    -7kg대 노르웨이 연어, 3kg대 참돔, 3kg대 농어, 대광어를 기본으로 제공하고 있습니다.
    
    -자체 숙성 기술을 통해서 숙성회 특유의 감칠맛을 끌어올리고 또한 쫀득한 식감을 만들어내며 어종별 상이한 숙성법을 통해서 고유의 맛과 향을 잘 느끼실 수 있게 작업합니다.
    
    ㅁ음식은 혀로 맛보기 전 눈으로 먼저 맛을 봅니다.
    
    -친환경 나무 용기, 대나무 잎 등의 자연 친화적인 재료를 사용하여 최대한 고급스러운 사시미 세트의 느낌을 제공합니다.
    
    -모든 조리 실장이 매번 음식, 숙성회, 담음새를 꼼꼼히 체크하여 정갈하며 깔끔한 플레이팅을 추구합니다.
    
    ㅁ숙성회136은 고객의 만족을 최우선에 두고 음식을 서비스합니다.
    
    -고객의 요청 사항을 최대한으로 들어드리기 위해서 항상 노력하고 있습니다."""
                
                total_response = response.text + pin_text
                #사장님 댓글 등록하기 클릭
                try:
                    # "사장님 댓글 등록하기" 버튼 클릭
                    comment_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.medium.secondary.self-ds'))
                    )
                    comment_button.click()
                    print("사장님 댓글 등록하기 버튼을 클릭했습니다.\n\n")
                except Exception as e:
                    print(f"버튼을 찾을 수 없습니다: {e}")
                
                # 텍스트 박스 클릭
                try:
                    text_area = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '(//textarea[contains(@class, "b_lv1quuv2_12i8sxie")])[2]'))
                    )
                    text_area.click()
                except Exception as e:
                    print(f"텍스트박스를 찾지 못했습니다: {e}")
                    
                print("===============================")
                print("AI가 답글을 생성했습니다. \n")
                print("손님 리뷰 내용:\n", review_text, "\n")
                print("AI의 답글 내용:\n", response.text, "\n")
                upload = input("등록할까요?  [yes = 1 / 수정 필요 = 0]\n")
                if upload == '1':
                    text_area.send_keys(total_response)
                    ## 여기에 등록버튼 누르기 하면 됨
                    try:
                        # 여러 클래스를 포함하는 요소를 찾기 위한 XPath
                        register_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "p.b_lv1quuv2_lv96zi7.b_lv1quuv2_1bisyd4a.b_lv1quuv2_1bisyd4r.b_lv1quuv2_1bisyd41z"))
                        )
                        register_button.click()
                    except Exception as e:
                        print(f"등록 버튼을 찾지 못했습니다: {e}")
                    ## 화면 새로고침
                    driver.refresh()
                    ## 기존화면 형태로 세팅
                    ad_pop_no_answer()
                elif upload == '0':
                    human_response = input("수정 내용을 입력해주세요\n")
                    regeneration = model.generate_content(response.text + "이게 너가 답한 대답이야 이거에 대해" + human_response)
                    print(regeneration.text)
                    total_response = regeneration.text + pin_text
                    text_area.send_keys(total_response)
                    try:
                        # 여러 클래스를 포함하는 요소를 찾기 위한 XPath
                        register_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "p.b_lv1quuv2_lv96zi7.b_lv1quuv2_1bisyd4a.b_lv1quuv2_1bisyd4r.b_lv1quuv2_1bisyd41z"))
                        )
                        register_button.click()
                    except Exception as e:
                        print(f"등록 버튼을 찾지 못했습니다: {e}")
                    ## 화면 새로고침
                    time.sleep(2)
                    driver.refresh()
                    ## 기존화면 형태로 세팅
                    ad_pop_no_answer()
                    print("수정 후 등록하였습니다.\n\n\n")
                else:
                    print("프로그램을 도중 탈출합니다.")
                    sys.exit(0)
    
            elif again == '0':
                print("프로그램을 종료합니다\n\n")
                sys.exit(0)
            else:
                print("1 또는 0을 입력해주세요.")
                
    #함수호출
    loop_answer()

if __name__ == "__main__":
    main()