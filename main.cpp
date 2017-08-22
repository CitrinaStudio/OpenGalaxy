// Copyright (c) 2017 phonphey
// 
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.


#include <cstdio>
#include <string>
#include "driver.h"
#include "cassandra/include/cassandra.h"

int main() {

    char* name;
    name = "dima";

    execute_cql(name);
    
    return 0;
}