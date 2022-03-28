#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2022 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to additional mode
netedit.additionalMode()

# select calibrator
netedit.changeElement("calibrator")

# create first calibrator
netedit.leftClick(referencePosition, 245, 140)

# create second calibrator
netedit.leftClick(referencePosition, 170, 280)

# go to inspect mode
netedit.inspectMode()

# inspect calibrator
netedit.leftClick(referencePosition, 300, 225)

# Change parameter id with a non valid value (Duplicated ID)
netedit.modifyAttribute(netedit.attrs.enums.calibrator.inspect.id, "ca_0", False)

# Change parameter id with a non valid value (Invalid ID)
netedit.modifyAttribute(netedit.attrs.enums.calibrator.inspect.id, "Id with spaces", False)

# Change parameter id with a valid value
netedit.modifyAttribute(netedit.attrs.enums.calibrator.inspect.id, "correctID", False)

# Check undos and redos
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
