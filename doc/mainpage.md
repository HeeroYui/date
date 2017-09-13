DATE library                                {#mainpage}
===============

@tableofcontents

What is DATE, and how can I use it?         {#date_mainpage_what}
====================================

Get the build date of the binary (simply externalyse to permit to not change the compilation flags of the program (just regenerate the SO and binary)

What languages are supported?                 {#date_mainpage_lang}
=============================

DATE is written in C++.

Are there any licensing restrictions?         {#date_mainpage_license_restriction}
=====================================

DATE is **FREE software** and _all sub-library are FREE and staticly linkable !!!_

License (MPL v2.0)                            {#date_mainpage_license}
==================

Copyright DATE Edouard DUPIN

Licensed under the Mozilla Public License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<https://www.mozilla.org/MPL/2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Usage?                                         {#date_mainpage_tutorial}
======

Use Date lib is really simple:

Include library header
```{.cpp}
#include <date/date.hpp>
```
Call the fucntion you need:
```{.cpp}
APPL_PRINT("Build year:" << date::getYear());
APPL_PRINT("Build month:" << date::getMonth());
APPL_PRINT("Build day:" << date::getDay());
APPL_PRINT("Build hour:" << date::getHour());
APPL_PRINT("Build minute:" << date::getMinute());
APPL_PRINT("Build second:" << date::getSecond());
// or :
APPL_PRINT("Build date:" << date::getDay() << "/" << date::getMonth() << "/" << date::getYear());
APPL_PRINT("Build time:" << date::getHour() << "h" << date::getMinute() << ":" << date::getSecond());
```

