import 'package:flet/flet.dart';

import 'flet_blur.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_blur":
      return BlurControl(
        parent: args.parent,
        control: args.control,
		backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
