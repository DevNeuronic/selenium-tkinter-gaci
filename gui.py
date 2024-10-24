�
    ag~  �                   �  � d Z ddlZddlZ	 ddlZddlZn# e$ r ddlmZ ddlm	Z Y nw xY wddl
Z
d� Zd� Z e�   �         Z G d� dej        �  �        Z G d� dej        �  �        Z G d	� d
ej        ej        �  �        Zedk    r�ddlZ	  eej        d         �  �        Zn# eef$ r dZY nw xY w ej         ee
j        de�  �        �  �        Z e de�!                    d�  �        �"                    �   �         �#                    �   �         z   �  �          e de�!                    d�  �        �"                    �   �         �#                    �   �         z   �  �         dS dS )z�
SocksiPy + urllib2 handler

version: 0.3
author: e<e@tr0ll.in>

This module provides a Handler which you can use with urllib2 to allow it to tunnel your connection through a socks.sockssocket socket, with out monkey patching the original socket...
�    Nc                 �X   � | �                     �   �         }|�                    |�  �         |S �N)�copy�update)�a�b�ds      �KC:\Users\tbanc\Desktop\Test_Selenium\venv\Lib\site-packages\sockshandler.py�
merge_dictr      s#   � �	�����A��H�H�Q�K�K�K��H�    c                 �   � 	 d| v r t          j        t           j        | �  �         nd| v rt          j        | �  �         ndS dS #  Y dS xY w)N�:�.FT)�socket�	inet_pton�AF_INET6�	inet_aton)�ss    r
   �is_ipr      sa   � �
��!�8�8���V�_�a�0�0�0�0��A�X�X���Q������5� �t����u�u���s   �=A �Ac                   �   � e Zd Zdd�Zd� ZdS )�SocksiPyConnectionNTc                 �T   � ||||||f| _         t          j        j        | g|�R i |�� d S r   )�	proxyargs�httplib�HTTPConnection�__init__�	�self�	proxytype�	proxyaddr�	proxyport�rdns�username�password�args�kwargss	            r
   r   zSocksiPyConnection.__init__+   s@   � �#�Y�	�4��8�T�����'��>�t�>�>�>�v�>�>�>�>�>r   c                 �  � | j         \  }}}}}}|o|t          v}	 	 t          j        | j        | j        f| j        d ||||||t          j        t          j	        dff�
  �
        }nb# t          j
        $ rO}|rBdt          |�  �        v r1t          | j        �  �        sd}t          �                    |�  �         n� Y d }~nd }~ww xY w��|| _        d S )NT�   �0x5bF)r   �socks4_no_rdns�socks�create_connection�host�port�timeoutr   �IPPROTO_TCP�TCP_NODELAY�SOCKS4Error�strr   �add�sock)	r   r   r    r!   r"   r#   r$   r5   �es	            r
   �connectzSocksiPyConnection.connect/   s  � �FJ�n�C��I�y�$��(��7�	��7��	���.��Y��	�*�D�L�$��y�)�T�8�X��(�&�*<�a�@�B�D� D�� ���$� � � �� �F�c�!�f�f�,�,�U�4�9�5E�5E�,� !�D�"�&�&�y�1�1�1�1�� 2�1�1�1�1���������	� ��	�	�	s   �AA# �#C�2AB<�<C�NTNN��__name__�
__module__�__qualname__r   r7   � r   r
   r   r   *   s7   � � � � � �?� ?� ?� ?�� � � � r   r   c                   �   � e Zd Zdd�Zd� ZdS )�SocksiPyConnectionSNTc                 �T   � ||||||f| _         t          j        j        | g|�R i |�� d S r   )r   r   �HTTPSConnectionr   r   s	            r
   r   zSocksiPyConnectionS.__init__D   s@   � �#�Y�	�4��8�T�����(��?��?�?�?��?�?�?�?�?r   c                 �  � t           �                    | �  �         | j        �                    | j        | j        ��  �        | _        | j        j        s�| j        r�	 t          j	        | j        �
                    �   �         | j        �  �         d S # t          $ r? | j        �                    t          j        �  �         | j        �                    �   �          � w xY wd S d S )N)�server_hostname)r   r7   �_context�wrap_socketr5   r-   �check_hostname�_check_hostname�ssl�match_hostname�getpeercert�	Exception�shutdownr   �	SHUT_RDWR�close)r   s    r
   r7   zSocksiPyConnectionS.connectH   s�   � ��"�"�4�(�(�(��M�-�-�d�i���-�S�S��	��}�+� 	��0D� 	���"�4�9�#8�#8�#:�#:�D�I�F�F�F�F�F��� � � ��	�"�"�6�#3�4�4�4��	���!�!�!������	� 	� 	� 	s   �1B �A	Cr8   r9   r=   r   r
   r?   r?   C   s;   � � � � � �@� @� @� @�	� 	� 	� 	� 	r   r?   c                   �    � e Zd Zd� Zd� Zd� ZdS )�SocksiPyHandlerc                 �`   � || _         || _        t          j        �                    | �  �         d S r   )r%   �kw�urllib2�HTTPHandlerr   )r   r%   r&   s      r
   r   zSocksiPyHandler.__init__T   s-   � ���	������$�$�T�*�*�*�*�*r   c                 �<   � � d� fd�	}� �                     ||�  �        S )Nr   c                 �\   �� t          �j        |�  �        }t          �j        | ||d�|��}|S �N)r-   r.   r/   )r   rR   r   r%   �r-   r.   r/   r&   rR   �connr   s         �r
   �buildz(SocksiPyHandler.http_open.<locals>.buildZ   s8   �� ��D�G�V�,�,�B�%�t�y�t�$�PW�^�^�[]�^�^�D��Kr   �Nr   ��do_open�r   �reqrZ   s   `  r
   �	http_openzSocksiPyHandler.http_openY   �7   �� �	� 	� 	� 	� 	� 	� �|�|�E�3�'�'�'r   c                 �<   � � d� fd�	}� �                     ||�  �        S )Nr   c                 �\   �� t          �j        |�  �        }t          �j        | ||d�|��}|S rW   )r   rR   r?   r%   rX   s         �r
   rZ   z)SocksiPyHandler.https_open.<locals>.builda   s8   �� ��D�G�V�,�,�B�&��	��4�QX�_�_�\^�_�_�D��Kr   r[   r\   r^   s   `  r
   �
https_openzSocksiPyHandler.https_open`   ra   r   N)r:   r;   r<   r   r`   rd   r=   r   r
   rP   rP   S   sA   � � � � � �+� +� +�
(� (� (�(� (� (� (� (r   rP   �__main__r(   iZ#  �	localhostzHTTP: zhttp://httpbin.org/ipzHTTPS: zhttps://httpbin.org/ip)$�__doc__r   rH   rS   r   �ImportError�urllib.request�request�http.client�clientr+   r   r   �setr*   r   r   rA   r?   rT   �HTTPSHandlerrP   r:   �sys�int�argvr.   �
ValueError�
IndexError�build_opener�PROXY_TYPE_SOCKS5�opener�print�open�read�decoder=   r   r
   �<module>r{      sD  ��� � ���� 
�
�
�
�"��N�N�N��N�N�N�N��� "� "� "�$�$�$�$�$�$�!�!�!�!�!�!�!�!�"���� ����� � �
� � � ������ � � � ��/� � � �2� � � � �'�1� � � � (� (� (� (� (�g�)�7�+?� (� (� (�( �z����J�J�J���s�3�8�A�;�������
�#� � � ���������!�W�!�/�/�%�2I�;�X\�"]�"]�^�^�F�	�E�(�V�[�[�!8�9�9�>�>�@�@�G�G�I�I�
I�J�J�J�	�E�)�f�k�k�":�;�;�@�@�B�B�I�I�K�K�
K�L�L�L�L�L� �s   � �)�)�
B! �!	B-�,B-