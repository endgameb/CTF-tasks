┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ base64 -d enc_flag
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='

┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ==" | base64 -d

wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}

запускаем расшифровку цезаря на си
┌──(kali㉿kali)-[~/Рабочий стол/CTF]
└─$ ./c
Shift: 1 -> voiuIZL{igkygx_j3ix9vz3j_86jk32j2}
Shift: 2 -> unhtHYK{hfjxfw_i3hw9uy3i_86ij32i2}
Shift: 3 -> tmgsGXJ{geiwev_h3gv9tx3h_86hi32h2}
Shift: 4 -> slfrFWI{fdhvdu_g3fu9sw3g_86gh32g2}
Shift: 5 -> rkeqEVH{ecguct_f3et9rv3f_86fg32f2}
Shift: 6 -> qjdpDUG{dbftbs_e3ds9qu3e_86ef32e2}
Shift: 7 -> picoCTF{caesar_d3cr9pt3d_86de32d2}
Shift: 8 -> ohbnBSE{bzdrzq_c3bq9os3c_86cd32c2}
Shift: 9 -> ngamARD{aycqyp_b3ap9nr3b_86bc32b2}
Shift: 10 -> mfzlZQC{zxbpxo_a3zo9mq3a_86ab32a2}
Shift: 11 -> leykYPB{ywaown_z3yn9lp3z_86za32z2}
Shift: 12 -> kdxjXOA{xvznvm_y3xm9ko3y_86yz32y2}
Shift: 13 -> jcwiWNZ{wuymul_x3wl9jn3x_86xy32x2}
Shift: 14 -> ibvhVMY{vtxltk_w3vk9im3w_86wx32w2}
Shift: 15 -> haugULX{uswksj_v3uj9hl3v_86vw32v2}
Shift: 16 -> gztfTKW{trvjri_u3ti9gk3u_86uv32u2}
Shift: 17 -> fyseSJV{squiqh_t3sh9fj3t_86tu32t2}
Shift: 18 -> exrdRIU{rpthpg_s3rg9ei3s_86st32s2}
Shift: 19 -> dwqcQHT{qosgof_r3qf9dh3r_86rs32r2}
Shift: 20 -> cvpbPGS{pnrfne_q3pe9cg3q_86qr32q2}
Shift: 21 -> buoaOFR{omqemd_p3od9bf3p_86pq32p2}
Shift: 22 -> atnzNEQ{nlpdlc_o3nc9ae3o_86op32o2}
Shift: 23 -> zsmyMDP{mkockb_n3mb9zd3n_86no32n2}
Shift: 24 -> yrlxLCO{ljnbja_m3la9yc3m_86mn32m2}
Shift: 25 -> xqkwKBN{kimaiz_l3kz9xb3l_86lm32l2}

флаг: picoCTF{caesar_d3cr9pt3d_86de32d2}
