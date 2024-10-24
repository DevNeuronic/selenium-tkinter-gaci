�
    v^g�  �                   ��   � d dl Z d dlZde j        v Zd� Zd� Zd� Zd� Zd� Z G d� d	�  �        Z	 G d
� d�  �        Z
e
j        D ]Z ee
de� �e
j        �  �         � e
�   �         Zd� Z G d� d�  �        Zd� Zd� ZdS )�    N�__pypy__c                  �   � dt           j        vrd S t          rt           j        dk     rd S dd l} | �                    d�  �         d S )N�	distutils)�   �   r   a�  Distutils was imported before Setuptools, but importing Setuptools also replaces the `distutils` module in `sys.modules`. This may lead to undesirable behaviors or errors. To avoid these issues, avoid using distutils directly, ensure that setuptools is installed in the traditional way (e.g. not an editable install), and/or make sure that setuptools is always imported before distutils.)�sys�modules�is_pypy�version_info�warnings�warn)r   s    �WC:\Users\tbanc\Desktop\Test_Selenium\venv\Lib\site-packages\_distutils_hack/__init__.py�warn_distutils_presentr   	   s^   � ��#�+�%�%���� �3�#�f�,�,� 	���O�O�O��M�M�	?�� � � � �    c                  �   � dt           j        vrd S dd l} | �                    d�  �         d� t           j        D �   �         }|D ]}t           j        |= �d S )Nr   r   z"Setuptools is replacing distutils.c                 �H   � g | ]}|d k    s|�                     d�  �        �|�� S )r   z
distutils.)�
startswith)�.0�names     r   �
<listcomp>z#clear_distutils.<locals>.<listcomp>"   s>   � � � � ���;���$�/�/�,�"?�"?�� 	���r   )r   r	   r   r   )r   �modsr   s      r   �clear_distutilsr      sx   � ��#�+�%�%����O�O�O��M�M�6�7�7�7�� ��K�� � �D�
 � � ���K����� r   c                  �N   � t           j        �                    dd�  �        } | dk    S )z?
    Allow selection of distutils by environment variable.
    �SETUPTOOLS_USE_DISTUTILS�local)�os�environ�get)�whichs    r   �enabledr    +   s%   � � �J�N�N�5�w�?�?�E��G��r   c                  �  � dd l } t          �   �          t          �   �         5  | �                    d�  �         d d d �  �         n# 1 swxY w Y   | �                    d�  �        }d|j        v sJ |j        �   �         �dt
          j        vsJ �d S )Nr   r   zdistutils.core�
_distutilszsetuptools._distutils.log)�	importlibr   �shim�import_module�__file__r   r	   )r#   �cores     r   �ensure_local_distutilsr(   3   s�   � ���������
 
��� -� -�����,�,�,�-� -� -� -� -� -� -� -� -� -� -���� -� -� -� -� �"�"�#3�4�4�D��4�=�(�(�(�$�-�(�(�(�&�c�k�9�9�9�9�9�9s   �A�A�
Ac                  �^   � t          �   �         rt          �   �          t          �   �          dS dS )z�
    Ensure that the local copy of distutils is preferred over stdlib.

    See https://github.com/pypa/setuptools/issues/417#issuecomment-392298401
    for more motivation.
    N)r    r   r(   � r   r   �do_overrider+   D   s8   � � �y�y� !�� � � �� � � � � �!� !r   c                   �   � e Zd Zd� Zd� ZdS )�
_TrivialRec                 �   � || _         d S �N)�	_patterns)�self�patternss     r   �__init__z_TrivialRe.__init__Q   s   � �!����r   c                 �D   �� t          �fd�| j        D �   �         �  �        S )Nc              3   �    �K  � | ]}|�v V � �	d S r/   r*   )r   �pat�strings     �r   �	<genexpr>z#_TrivialRe.match.<locals>.<genexpr>U   s'   �� � � �;�;�S�3�&�=�;�;�;�;�;�;r   )�allr0   )r1   r7   s    `r   �matchz_TrivialRe.matchT   s(   �� ��;�;�;�;�D�N�;�;�;�;�;�;r   N)�__name__�
__module__�__qualname__r3   r:   r*   r   r   r-   r-   P   s2   � � � � � �"� "� "�<� <� <� <� <r   r-   c                   �   � e Zd Zdd�Zd� Zed� �   �         Zd� Zed� �   �         Z	ed� �   �         Z
d� Zej        d	k     rg d
�ndgZdS )�DistutilsMetaFinderNc                 �   � |�|�                     d�  �        sd S  dj        di t          �   �         ��}t          | |d� �  �        } |�   �         S )Nztest.zspec_for_{fullname}c                  �   � d S r/   r*   r*   r   r   �<lambda>z/DistutilsMetaFinder.find_spec.<locals>.<lambda>`   s   � �D� r   r*   )r   �format�locals�getattr)r1   �fullname�path�target�method_name�methods         r   �	find_speczDistutilsMetaFinder.find_specY   s]   � � ��H�$7�$7��$@�$@���F�2�+�2�>�>�V�X�X�>�>����{�L�L�9�9���v�x�x�r   c                 �   �� | �                     �   �         rd S dd l}dd l}dd l}	 |�                    d�  �        �n# t
          $ r Y d S w xY w G �fd�d|j        j        �  �        }|j        �	                    d |�   �         �j
        ��  �        S )Nr   zsetuptools._distutilsc                   �    �� e Zd Z� fd�Zd� ZdS )�?DistutilsMetaFinder.spec_for_distutils.<locals>.DistutilsLoaderc                 �   �� d�_         �S )Nr   )r;   )r1   �spec�mods     �r   �create_modulezMDistutilsMetaFinder.spec_for_distutils.<locals>.DistutilsLoader.create_moduley   s   �� �*����
r   c                 �   � d S r/   r*   )r1   �modules     r   �exec_modulezKDistutilsMetaFinder.spec_for_distutils.<locals>.DistutilsLoader.exec_module}   s   � ��r   N)r;   r<   r=   rR   rU   )rQ   s   �r   �DistutilsLoaderrN   x   s=   �� � � � � �� � � � �� � � � r   rV   r   )�origin)�
is_cpythonr#   �importlib.abc�importlib.utilr%   �	Exception�abc�Loader�util�spec_from_loaderr&   )r1   r#   rV   rQ   s      @r   �spec_for_distutilsz&DistutilsMetaFinder.spec_for_distutilsc   s�   �� ��?�?��� 	��F�������������	��)�)�*A�B�B�C�C��� 		� 		� 		� �F�F�		����	� 	� 	� 	� 	� 	� 	�i�m�2� 	� 	� 	� �~�.�.����*�*�3�<� /� 
� 
� 	
s   �; �
A	�A	c                  �@   � t           j        �                    d�  �        S )zj
        Suppress supplying distutils for CPython (build and tests).
        Ref #2965 and #3007.
        zpybuilddir.txt)r   rG   �isfiler*   r   r   rX   zDistutilsMetaFinder.is_cpython�   s   � � �w�~�~�.�/�/�/r   c                 �^   � | �                     �   �         rdS t          �   �          d� | _        dS )zj
        Ensure stdlib distutils when running under pip.
        See pypa/pip#8761 for rationale.
        Nc                  �   � d S r/   r*   r*   r   r   rB   z2DistutilsMetaFinder.spec_for_pip.<locals>.<lambda>�   �   � �$� r   )�pip_imported_during_buildr   r`   �r1   s    r   �spec_for_pipz DistutilsMetaFinder.spec_for_pip�   s9   � �
 �)�)�+�+� 	��F�����".�,����r   c                 �h   � � ddl }t          � fd�|�                    d�  �        D �   �         �  �        S )zO
        Detect if pip is being imported in a build script. Ref #2355.
        r   Nc              3   �H   �K  � | ]\  }}��                     |�  �        V � �d S r/   )�frame_file_is_setup)r   �frame�line�clss      �r   r8   z@DistutilsMetaFinder.pip_imported_during_build.<locals>.<genexpr>�   sF   �� � � � 
� 
�/:�u�d�C�#�#�E�*�*�
� 
� 
� 
� 
� 
r   )�	traceback�any�
walk_stack)rn   ro   s   ` r   rf   z-DistutilsMetaFinder.pip_imported_during_build�   sX   �� �
 	����� 
� 
� 
� 
�>G�>R�>R�SW�>X�>X�
� 
� 
� 
� 
� 	
r   c                 �^   � | j         �                    dd�  �        �                    d�  �        S )zN
        Return True if the indicated frame suggests a setup.py file.
        r&   � zsetup.py)�	f_globalsr   �endswith)rl   s    r   rk   z'DistutilsMetaFinder.frame_file_is_setup�   s*   � � ��"�"�:�r�2�2�;�;�J�G�G�Gr   c                 �2   � t          �   �          d� | _        dS )zp
        Ensure stdlib distutils when running select tests under CPython.

        python/cpython#91169
        c                  �   � d S r/   r*   r*   r   r   rB   z>DistutilsMetaFinder.spec_for_sensitive_tests.<locals>.<lambda>�   re   r   N)r   r`   rg   s    r   �spec_for_sensitive_testsz,DistutilsMetaFinder.spec_for_sensitive_tests�   s    � � 	����".�,����r   )r   �
   )�test.test_distutilsztest.test_peg_generatorztest.test_importlibrz   r/   )r;   r<   r=   rK   r`   �staticmethodrX   rh   �classmethodrf   rk   rx   r   r   �sensitive_testsr*   r   r   r?   r?   X   s�   � � � � � �� � � �
� 
� 
�B �0� 0� �\�0�/� /� /� �
� 
� �[�
� �H� H� �\�H�/� /� /� ��g�%�%�	
� 	
� 	
� 	
� "�
� �O�Or   r?   �	spec_for_c                  �N   � t           t          j        v pt          �   �          d S  d S r/   )�DISTUTILS_FINDERr   �	meta_path�insert_shimr*   r   r   �add_shimr�   �   s$   � ����%�6�������6�6�6r   c                   �   � e Zd Zd� Zd� ZdS )r$   c                 �"   � t          �   �          d S r/   )r�   rg   s    r   �	__enter__zshim.__enter__�   �   � ������r   c                 �"   � t          �   �          d S r/   )�remove_shim)r1   �exc�value�tbs       r   �__exit__zshim.__exit__�   r�   r   N)r;   r<   r=   r�   r�   r*   r   r   r$   r$   �   s2   � � � � � �� � �� � � � r   r$   c                  �P   � t           j        �                    dt          �  �         d S )Nr   )r   r�   �insertr�   r*   r   r   r�   r�   �   s!   � ��M����,�-�-�-�-�-r   c                  �r   � 	 t           j        �                    t          �  �         d S # t          $ r Y d S w xY wr/   )r   r�   �remover�   �
ValueErrorr*   r   r   r�   r�   �   sF   � ������-�.�.�.�.�.��� � � �������s   �$( �
6�6)r   r   �builtin_module_namesr
   r   r   r    r(   r+   r-   r?   r}   r   �setattrrx   r�   r�   r$   r�   r�   r*   r   r   �<module>r�      s{  �� 
�
�
�
� 	�	�	�	� ��0�
0��� � �&� � �� � �:� :� :�"	!� 	!� 	!�<� <� <� <� <� <� <� <�d� d� d� d� d� d� d� d�N  �/� � �D��G���D����4�� � � � '�&�(�(� �7� 7� 7�� � � � � � � �.� .� .�� � � � r   