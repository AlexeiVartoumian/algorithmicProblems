
import re 


demotext = """collap=\r\nse; border-spacing: 0; mso-table-lspace: 0; mso-table-rspace: 0; table-layo=\r\nut: fixed; vertical-align: middle; width: 100%;\" valing=3D\"middle\">\r\n                  =20\r\n                     <tbody>\r\n                   =20\r\n                     =20\r\n\r\n                    =20\r\n\r\n                   =20\r\n                    <tr>\r\n                   =20\r\n                        <td class=3D\"p2b\" style=3D\"direction:ltr;text-align=\r\n:left;color: #000000; font-family: 'UberMoveText-Bold', 'HelveticaNeueMediu=\r\nm', 'HelveticaNeue-Medium', 'Helvetica Neue Medium', Helvetica, Arial, sans=\r\n-serif; font-size: 20px; font-weight: bold; line-height: 26px; padding-bott=\r\nom: 0; padding-top: 0;\">1441</td>\r\n                     </tr>\r\n                    =20\r\n\r\n                  </tbody></table>\r\n               </td>\r\n            </tr>\r\n         </tbody></table>\r\n         <!--[if (gte mso 9)|(IE)]>\r\n      </td>\r\n   </tr>\r\n</table>\r\n<![endif]-->\r\n\r\n                        </td>\r\n                     </tr>\r\n                  </tbody></table>\r\n               </td>\r\n            </tr>\r\n         </tbody></table>\r\n         <!--[if (gte mso 9)|(IE)]>\r\n      </td>\r\n   </tr>\r\n</table>\r\n<![endif]-->\r\n               </td>\r\n            </tr>\r\n         </tbody></table>\r\n      </td>\r\n   </tr>\r\n</tbody></table>\r\n<!-- close Em7  mod 2 cuscat_2019/09/7  -->=20\r\n=20\r\n<!-- Em7 Module 3 cuscat_2019/09/7  -->=20\r\n<table width=3D\"100%\" border=3D\"0\" cellpadding=3D\"0\" cellspacing=3D\"0\" styl=\r\ne=3D\"background-color: #F3F8FF; border: none; border-collapse: collapse; bo=\r\nrder-spacing: 0; mso-table-lspace: 0; mso-table-rspace: 0; width: 100%;\">\r\n   <tbody><tr>\r\n      <td class=3D\"outsidegutter\" align=3D\"left\" style=3D\"direction:ltr;tex=\r\nt-align:left;padding: 0 14px 0 14px;\">\r\n         <table border=3D\"0\" cellpadding=3D\"0\" cellspacing=3D\"0\" style=3D\"b=\r\norder: none; border-collapse: collapse; border-spacing: 0; mso-table-lspace=\r\n: 0; mso-table-rspace: 0; width: 100%;\" class=3D\"\">\r\n            <tbody><tr>\r\n               <td style=3D\"direction:ltr;text-align:left;padding-"""

def extract_numbers(text):
    """
    match a specific pattern
    """


    pattern = r'; padding-top: 0;">(\d{4})</td>'

    matches = re.findall(pattern, text)

    return matches


print(extract_numbers(demotext))
